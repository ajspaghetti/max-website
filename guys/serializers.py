from rest_framework import serializers
from .models import Guy

class GuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Guy
        fields = ['id', 'first_name', 'last_name', 'job_title', 'company', 'bio']