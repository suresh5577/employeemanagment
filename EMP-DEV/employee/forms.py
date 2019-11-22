from django import forms
from .models import Projects, Department



class DepartmentForm(forms.Form):
    dep_name = forms.CharField(label="Department Name ", max_length=100)

'''
class ProjectForm(forms.Form):
    project_name = forms.CharField(label='Project Name', max_length=100)
    client_name = forms.CharField(label='Client Name', max_length=100)
    contact_person = forms.CharField(label='Contact Person Name', max_length=100)
    contact_person_email = forms.EmailField(label='Contact Person Email', )
'''

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_name', 'client_name', 'contact_person']

class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    projects = forms.ModelChoiceField(queryset=Projects.objects.all())
    designation = forms.CharField(max_length=100)
    about_employee = forms.CharField(widget=forms.Textarea)
    joining_date = forms.DateField()
    birth_date = forms.DateField()
    #relieving_date = forms.DateField()    
    salary = forms.IntegerField()
    total_experience = forms.FloatField()
