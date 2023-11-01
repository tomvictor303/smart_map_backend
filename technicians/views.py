from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from technicians.models import Technician
from technicians.serializers import TechnicianSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def technician_list(request):
    if request.method == 'GET':
        technicians = Technician.objects.all()
        
        # title = request.GET.get('title', None)
        # if title is not None:
        #     technicians = technicians.filter(title__icontains=title)
        
        technicians_serializer = TechnicianSerializer(technicians, many=True)
        return JsonResponse(technicians_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        technician_data = JSONParser().parse(request)
        technician_serializer = TechnicianSerializer(data=technician_data)
        if technician_serializer.is_valid():
            technician_serializer.save()
            return JsonResponse(technician_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(technician_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Technician.objects.all().delete()
        return JsonResponse({'message': '{} Technicians were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def technician_detail(request, pk):
    try: 
        technician = Technician.objects.get(pk=pk) 
    except Technician.DoesNotExist: 
        return JsonResponse({'message': 'The technician does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        technician_serializer = TechnicianSerializer(technician) 
        return JsonResponse(technician_serializer.data) 
 
    elif request.method == 'PUT': 
        technician_data = JSONParser().parse(request) 
        technician_serializer = TechnicianSerializer(technician, data=technician_data) 
        if technician_serializer.is_valid(): 
            technician_serializer.save() 
            return JsonResponse(technician_serializer.data) 
        return JsonResponse(technician_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        technician.delete() 
        return JsonResponse({'message': 'Technician was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

