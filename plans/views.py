from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from plans.models import Plan
from plans.serializers import PlanSerializer
from rest_framework.decorators import api_view
from django.db import connection

@api_view(['GET', 'POST', 'DELETE'])
def plan_list(request):
    if request.method == 'GET':
        plans = Plan.objects.all()
        
        plans_serializer = PlanSerializer(plans, many=True)
        return JsonResponse(plans_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        params = JSONParser().parse(request)
        plan_serializer = PlanSerializer(data=params)
        if not plan_serializer.is_valid():            
          return JsonResponse(plan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Save only if it does not already exists
        exists = Plan.objects.filter(person=params['person'], date=params['date'], task=params['task'])
        if exists.count():
          first_exist_serializer = PlanSerializer(exists[0])
          return JsonResponse(first_exist_serializer.data, status=status.HTTP_201_CREATED) 
        else:
          plan_serializer.save()
        return JsonResponse(plan_serializer.data, status=status.HTTP_201_CREATED) 
 
@api_view(['POST'])
def plan_smart_delete(request):
    if request.method == 'POST':
        params = JSONParser().parse(request)
        if not params.get('person') or not params.get('date') or not params.get('priorities'):
          return JsonResponse({'message': 'Some parameters are missed or null!'}, status=status.HTTP_400_BAD_REQUEST)
        # search and delete
        count = Plan.objects.filter(person=params['person'], date=params['date'], task=params['task']).delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def plan_priorities_update(request):
    # {
    #     "person": 1,
    #     "date": "2023-10-02",
    #     "priorities": {
    #         "5": 111,
    #         "7": 133,
    #         "8": 135
    #     }
    # }
    if request.method == 'POST':
        params = JSONParser().parse(request)

        if not params.get('person') or not params.get('date') or not params.get('priorities'):
          return JsonResponse({'message': 'Some parameters are missed or null!'}, status=status.HTTP_400_BAD_REQUEST)
        
        priorities = params.get('priorities')
        if not type(priorities) is dict:
          return JsonResponse({'message': 'Priorities parameter must be dictionary'}, status=status.HTTP_400_BAD_REQUEST)
        
        case_sql = "CASE "
        for key in priorities:
          case_sql += "WHEN task=" + key + " THEN " + str(priorities[key]) + " " 
        case_sql += " ELSE priority END"

        db_table_name = Plan.objects.model._meta.db_table
        sql = f"UPDATE {db_table_name} SET priority = ({case_sql}) WHERE person={params['person']} AND date='{params['date']}'"

        with connection.cursor() as cursor:
          cursor.execute(sql)
        return JsonResponse({'message': 'ok', 'sql': sql}, status=status.HTTP_200_OK) 
