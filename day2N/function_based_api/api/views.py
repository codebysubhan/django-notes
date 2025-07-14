from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize
from .serializer import StudentSerializer
from .models import Student

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE']) # default is get even if nothing written here like: @api_view
def hello_world(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated at ' + str(request.data.get('id'))})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data updated at ' + str(pk)})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted Success at '+str(id)})

