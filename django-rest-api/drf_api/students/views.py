from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer

@api_view(['get'])
def student_list(requset):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many = True)
    return Response(serializer.data)