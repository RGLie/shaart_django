from rest_framework import serializers
from bson import ObjectId
from .models import CustomUser
from rest_framework import serializers
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'solved_problems', 'solving_problems']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()




class SolvedProblemSerializer(serializers.Serializer):
    problem_id = serializers.IntegerField()


class ProblemIDSerializer(serializers.Serializer):
    problem_id = serializers.IntegerField()