from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet, basename="product")
app_name = 'product'
urlpatterns = [
    path('', include(router.urls)),
]