from django.urls import path, include
from .views import data

from rest_framework.routers import DefaultRouter

from .views import CompanyView

router = DefaultRouter()
router.register('company', CompanyView)

urlpatterns = [
    path('k/', data),
    path('', include(router.urls))

]