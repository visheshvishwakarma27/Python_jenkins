from dataclasses import field
from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    choice=(('male','MALE',),('female','FEMALE',))
    name=serializers.CharField()
    contact=serializers.IntegerField()
    gender=serializers.ChoiceField(choices=choice)

    class Meta:
        model=Person
        fields = '__all__'
    