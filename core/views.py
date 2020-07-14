from .services import get_companies
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import mixins, generics
from .serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Company


def data(request):
    """ Company API """
    k_data = get_companies()
    Company.objects.create(data=k_data)
    return JsonResponse(data=k_data,safe=False)


class CompanyView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get_queryset(self):
        return self.queryset.filter()
