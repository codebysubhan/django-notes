from django.shortcuts import render
from yaml import serialize

from day11.djangotutorial.mysite.asgi import application
from .models import Student
from .serializer import StudentSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
# Create your views here.

def list_one_std(request, pk):
    std_obj = Student.objects.get(pk = pk) # Dtype = 'api1.models.Student'
    serializer = StudentSerializer(std_obj)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def list_all_students(request):
    stds_obj = Student.objects.all()
    serializer  = StudentSerializer(stds_obj, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
