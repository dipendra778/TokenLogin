from .models import LoginModel,NestedModel
from rest_framework import serializers

class NestedSerializer(serializers.ModelSerializer):
    class Meta:
        model=NestedModel
        fields=('id','age','speciality')

class LoginSerializer(serializers.ModelSerializer):
    login = NestedSerializer()
    class Meta:
        model=LoginModel
        fields=('name','phone','address','login')

    def create(self, validated_data):
        login_data =validated_data.pop('login')
        login = NestedModel.objects.create(**login_data)
        nested = LoginModel.objects.create(login=login, **validated_data)
        return nested

    def update(self, instance, validated_data):
        login_data =validated_data.pop('login')
        instance.name=validated_data.get("name",instance.name)
        instance.phone=validated_data.get("phone",instance.phone)
        instance.address=validated_data.get("address",instance.address)
        instance.save()

        return instance
 #  keep_login=[]
       # # if "id" in login_data.keys():
       #  if LoginModel.objects.filter(id=login_data["id"].exists()):
       #      l=LoginModel.objects.get(id=login_data["id"])
       #      l.age=login_data.get('age',l.age)
       #      l.speciality=login_data.get('speciality',l.speciality)
       #      l.save()
       #      keep_login.append(l)