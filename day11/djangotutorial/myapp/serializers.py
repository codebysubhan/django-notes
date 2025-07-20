from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializer.CharField(max_length=100)
    roll = serializer.IntegerField()
    city = serializer.CharField(max_length=100)


#serializer = StudentSerializer(stu)
