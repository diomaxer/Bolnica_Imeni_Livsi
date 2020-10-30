from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    # title = serializers.CharField(max_length=120)
    # description = serializers.CharField()
    # body = serializers.CharField()
    # author_id = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password',
            'city',
            'company',
            'avatar',
        ]

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.city = validated_data.get('city', instance.city)
        instance.company = validated_data.get('company', instance.company)
        instance.avatar = validated_data.get('avatar', instance.avatar)

        instance.save()
        return instance