from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Teachers
from .serializers import TeacherSerializer

class TeachersApi(APIView):
    # get data
    def get(self, request, id = None):
        if id:
            try:
                # single data based on ID
                teacher = Teachers.objects.get(id = id)
                serializer = TeacherSerializer(teacher)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except teacher.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        else:
            # else all teacher data
            teacher = Teachers.objects.all()
            serializer = TeacherSerializer(teacher, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # post data
    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    # update data
    def put(self, request, id):
        try:
            teacher = Teachers.objects.get(id = id)
        except Teachers.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeacherSerializer(teacher, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # patch update
    def patch(self, request, id):
        try:
            teacher = Teachers.objects.get(id = id)
        except Teachers.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
                
        serializer = TeacherSerializer(teacher, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # delete data
    def delete(self, request, id):
        try:
            teacher = Teachers.objects.get(id=id)
            teacher.delete()
            return Response(status = status.HTTP_200_OK)
        except Teachers.DoesNotExist:
            return Response({"error": "Teacher not found"}, status = status.HTTP_404_NOT_FOUND)