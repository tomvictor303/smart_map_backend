from rest_framework import serializers 
from plans.models import Plan
 
 
class PlanSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Plan
        fields = ('id',
                  'task',
                  'person',
                  'date'
                  'priority')
