from rest_framework import serializers 
from user.models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'




class Skillserializer(serializers.ModelSerializer):
    #user=Userserializer()
    class Meta:
        model = Skill
        fields = '__all__'
        