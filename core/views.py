from .services import get_companies
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from django.http import JsonResponse

def data(request):
    """ Company API """
    k_data = get_companies()
    return JsonResponse(k_data,safe=False)
