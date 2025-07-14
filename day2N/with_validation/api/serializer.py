# from attr.filters import exclude
from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    # def validate_with_r(value):
    #     if value[0].lower() != 'r':
    #         print('hereeeee')
    #         raise serializers.ValidationError("Name should Start with r!")
        # return value
    # name = serializers.CharField(read_only=True)
    # name = serializers.CharField(validators=[validate_with_r])
    class Meta:
        model = Student
        # fields = '__all__' # for all attributes
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name']
        # fields = exclude('id') # for all except 'id'
        # we can also write like:
        # extra_kwargs = {'name':{'read_only':True}}
    def validate_name(self, value):
        print("validate_name called with:", value)
        if value[0].lower()!='r':
            print('condition true')
            raise serializers.ValidationError("name should statr with r")
        return value
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
#
