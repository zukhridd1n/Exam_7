from rest_framework.viewsets import ModelViewSet

from vacancy.filters import FilterBackend
from vacancy.models import Vacancy
from vacancy.serializers import VacancySerializer


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all().order_by('id')
    serializer_class = VacancySerializer
    filter_backends = (FilterBackend, )
    filter_fields = ('salary',)
