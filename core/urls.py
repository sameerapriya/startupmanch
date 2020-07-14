from django.urls import path
from .views import *

urlpatterns = [
    path('k/',SwaggerSchemaView.as_view() ),
]