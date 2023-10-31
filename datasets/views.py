from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
import csv
import os

@api_view(['GET'])
def task_list(request):
    if request.method == 'GET':
        rows = []
        # load cluster dataset
        with open(os.getcwd() + '/datasets/assets/out.nt_yards.csv', newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
              rows.append({ 
                 **row,
                 'id': 'cluster_' + row['lat'] + '_' + row['lon'],
                 'dataset': 'cluster' 
              })
        # load device dataset
        with open(os.getcwd() + '/datasets/assets/out.brick_devices.csv', newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
              rows.append({ 
                 **row,
                 'id': 'device_' + row['lat'] + '_' + row['lon'],
                 'dataset': 'device' 
              })
        return JsonResponse(rows, safe=False)
        # 'safe=False' for objects serialization
 