from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vacancy.views import VacancyViewSet

router = DefaultRouter()
router.register('', VacancyViewSet, basename="vacancy")
app_name = 'vacancy'
urlpatterns = [
    path('', include(router.urls)),
]