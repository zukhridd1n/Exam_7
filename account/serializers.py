from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from account.models import Account



class AccountSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError("Passwords must be match")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        account: Account = super().create(validated_data)
        account.set_password(validated_data["password"])
        account.save()
        return account

    class Meta:
        model = Account
        fields = ("id", "username", "email", "password", "password2", "first_name", "last_name", "is_deleted")
        extra_kwargs = {
            'email': {'required': True, 'allow_null': False},
            'first_name': {'required': True, 'allow_null': False},
            'last_name': {'required': True, 'allow_null': False}
        }

