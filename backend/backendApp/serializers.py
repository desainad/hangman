from rest_framework import serializers
from .models import s_movie

class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = s_movie
        fields = '__all__'
