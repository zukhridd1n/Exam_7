from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post.views import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet, basename="post")
app_name = 'post'
urlpatterns = [
    path('', include(router.urls)),
]