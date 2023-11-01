from rest_framework import serializers 
from technicians.models import Technician
 
 
class TechnicianSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Technician
        fields = ('id',
                  'first_name',
                  'last_name',
                  'lat',
                  'lon')
