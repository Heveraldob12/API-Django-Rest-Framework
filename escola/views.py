from django.http import JsonResponse
from rest_framework import viewsets
from escola.models import Aluno, Curso,Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
