from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import UserProfile, Event, Club, Workshop, Announcement


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        UserProfile.objects.create(user=user, role='student')
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

class AdminSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    secret_code = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['username','email','password','secret_code']
        
    def validate_secret_code(self,value):
        if value != 'CAMPUS@ADMIN2024':
            raise serializers.ValidationError('Invalid secret code!')
        return value
            
    def create(self, validated_data):
        validated_data.pop('secret_code')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            )
        UserProfile.objects.create(user=user, role='admin')
        return user
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'
        
class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

    
