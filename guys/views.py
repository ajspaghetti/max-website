from django.http import JsonResponse
from .models import Guy
from .serializers import GuySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST']) 
def guy_list(request, format=None):
    
    if request.method == 'GET':
        guys = Guy.objects.all() #get all the guys
        serializer = GuySerializer(guys, many=True) #serialize them
        return Response(serializer.data) #return json #, safe=False
    
    if request.method == 'POST':
        serializer = GuySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def guy_detail(request, id, format=None):
    
    try:
        guy = Guy.objects.get(pk=id)
    except Guy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = GuySerializer(guy)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GuySerializer(guy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        guy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)