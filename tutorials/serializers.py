from rest_framework import serializers
from .models import  UserProfile,Tutorial


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

    def validate_title(self, value):
        # Perform validation logic for the title field
        if len(value) < 1:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    def validate_description(self, value):
        # Perform validation logic for the description field
        if len(value) < 1:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        return value


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to the token payload, if needed
        token['custom_key'] = 'custom_value'

        return token
