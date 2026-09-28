from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Users
from .serializers import UsersSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    serailizer = UsersSerializer(users, many = True)
    return Response(serailizer.data)

@api_view(['post'])
def add_users(request):
    serializer = UsersSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['put', 'patch'])
def update_user(request, id):
    try:
        user = Users.objects.get(id = id)
    except Users.DoesNotExist:
        return Response({'error': "Student Not Found"}, status= status.HTTP_400_BAD_REQUEST)

    # partial update support (PATCH api)
    if request.method == 'PATCH':
        serializer = UsersSerializer(user, data = request.data, partial=True)
    else:
        serializer = UsersSerializer(user, data = request.data)
    
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['delete'])
def delete_user(request, id):
    try:
        user = Users.objects.get(id = id)
    except Users.DoesNotExist:
            return Response({'error': "Student Not Found"}, status= status.HTTP_400_BAD_REQUEST)

    user.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)