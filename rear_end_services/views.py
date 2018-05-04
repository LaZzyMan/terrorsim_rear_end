from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import GlobalTerrorism
from .serializers import GlobalTerrorismSerializer
# Create your views here.


@api_view(['GET', ])
def terrorism_info(request, id, format=None):
    '''
    Get terrorism information by id
    '''
    try:
        target = GlobalTerrorism.objects.get(id=id)
    except GlobalTerrorism.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(GlobalTerrorismSerializer(target).data)
