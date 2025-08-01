import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializer import StudentSerializer
from rest_framework.parsers import JSONParser
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)  # python_data is dict()
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            json_data = {
                'response': 'success'
            }
            json_data = JSONRenderer().render(json_data)
            return HttpResponse(json_data, content_type='application/json')
        json_data = serializer.errors
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated success'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = serializer.errors
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
#
# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id', None) # python_data is dict()
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer  = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             json_data = {
#                 'response': 'success'
#             }
#             json_data = JSONRenderer().render(json_data)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = serializer.errors
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=python_data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data updated success'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = serializer.errors
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'DELETE':
#         print('hereeeeeeeeeeee')
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg':'Data Deleted!'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')