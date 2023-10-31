from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from plans.models import Plan
from plans.serializers import PlanSerializer, PlanPrioritySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def plan_list(request):
    if request.method == 'GET':
        plans = Plan.objects.all()
        
        plans_serializer = PlanSerializer(plans, many=True)
        return JsonResponse(plans_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        plan_data = JSONParser().parse(request)
        plan_serializer = PlanSerializer(data=plan_data)
        if plan_serializer.is_valid():
            plan_serializer.save()
            return JsonResponse(plan_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(plan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        to_delete_id = request.GET.get('id', None)
        if to_delete_id is not None:
            count = Plan.objects.filter(id=to_delete_id)
            return JsonResponse({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({'message': 'Item with provided ID is not exist!'}, status=status.HTTP_204_NO_CONTENT)
 
