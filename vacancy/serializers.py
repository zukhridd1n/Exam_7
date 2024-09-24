from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from account.models import Account
from vacancy.models import Vacancy


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'salary')

