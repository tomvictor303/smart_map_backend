from rest_framework import serializers 
from technicians.models import Technician
 
 
class TechnicianSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Technician
        fields = ('id',
                  'title',
                  'description',
                  'published')
