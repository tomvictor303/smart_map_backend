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
        if not plan_serializer.is_valid():            
          return JsonResponse(plan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Save only if it does not already exists
        exists = Plan.objects.filter(person=plan_data['person'], date=plan_data['date'], task=plan_data['task'])
        if exists.count():
          first_exist_serializer = PlanSerializer(exists[0])
          return JsonResponse(first_exist_serializer.data, status=status.HTTP_201_CREATED) 
        else:
          plan_serializer.save()
        return JsonResponse(plan_serializer.data, status=status.HTTP_201_CREATED) 
 
@api_view(['POST'])
def plan_smart_delete(request):
    if request.method == 'POST':
        plan_data = JSONParser().parse(request)
        count = Plan.objects.filter(person=plan_data['person'], date=plan_data['date'], task=plan_data['task']).delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
