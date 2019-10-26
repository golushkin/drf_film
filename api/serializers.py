from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Man, Film


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=False, default='')
    auth_token = serializers.StringRelatedField(read_only=True, default='')

    class Meta:
        model = get_user_model()
        fields = ('id','username', 'email', 'password','auth_token')

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class ManSerializer(serializers.ModelSerializer):
    played_films = serializers.StringRelatedField(many=True, read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)
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
        