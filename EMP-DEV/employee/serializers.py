from rest_framework import serializers
from .models import Projects



class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['project_name', 'client_name', 'contact_person', 'contact_person_email']