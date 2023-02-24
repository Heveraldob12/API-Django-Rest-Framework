from rest_framework import viewsets, generics,status
from escola.models import Aluno, Curso,Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2,CursoSerializer, MatriculaSerializer,ListaAlunosMatriculadosSerializer ,ListaMatriculasAlunoSerializer
from rest_framework.response import Response

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer
class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data,status=status.HTTP_201_CREATED) 
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
        
class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
