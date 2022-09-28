from random import choices
from urllib import request
from rest_framework import serializers
from .models import User, ContactDetails, Post


class ContactDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactDetails
        fields = ['primary_phone', 'secondary_phone',
                  'primary_email', 'secondary_email', 'address', ]


class UserRegisterSerializer(serializers.Serializer):
    details = ContactDetailsSerializer()
    password = serializers.CharField(
        min_length=6)
    username = serializers.CharField(
        min_length=6)
    image = serializers.ImageField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    role = serializers.ChoiceField(
        label="Role", choices=(('admin', 1), ('teacher', 2), ('student', 3)),
    )

    def create(self, validated_data):
        print(validated_data)
        print(validated_data.get("details"))
        details = validated_data.pop("details")
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        ContactDetails.objects.create(
            user_id=user.id, **details)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=130)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'description']
