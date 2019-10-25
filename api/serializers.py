from rest_framework import serializers
from .models import Man, Film


class ManSerializer(serializers.ModelSerializer):
    played_films = serializers.StringRelatedField(many=True, read_only=True)
    date_of_born = serializers.CharField(max_length=30,
                                         allow_null=True,
                                         required=False)
    class Meta:
        model = Man
        fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField(many=True, read_only=True)
    producer = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Film
        fields = '__all__'
        