from rest_framework import serializers 
from plans.models import Plan, PlanPriority
 
 
class PlanSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Plan
        fields = ('id',
                  'task',
                  'person',
                  'date')

class PlanPrioritySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = PlanPriority
        fields = ('id',
                  'priorities',
                  'person',
                  'date')
