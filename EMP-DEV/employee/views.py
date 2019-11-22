from django.shortcuts import render, HttpResponse
from .forms import DepartmentForm, ProjectModelForm, EmployeeForm
from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response



def addDepartment(request):
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():
            dep_name = request.POST.get('dep_name')
            depModelObj = Department(name=dep_name)
            depModelObj.save()

            return HttpResponse("<h3>Department Saved Successfully!!!</h3>")

    else:
        form = DepartmentForm()
    
    return render(request, 'genericForm.html', {'form': form})

'''
def addProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project_name = request.POST.get('project_name')
            client_name = request.POST.get('client_name')
            contact_person = request.POST.get('contact_person')
            contact_person_email = request.POST.get('contact_person_email')

            projModelObj = Projects(project_name=project_name, client_name=client_name, 
                                    contact_person=contact_person, contact_person_email=contact_person_email)
            projModelObj.save()
            
            return HttpResponse("<h3>Projects Saved Successfully!!!</h3>")

    else:
        form = ProjectForm()
    
    return render(request, 'genericForm.html', {'form': form})
'''

def addProject(request):
    if request.method == 'POST':
        form = ProjectModelForm(request.POST)

        if form.is_valid():
            #single line to save data into database
            #form.save()


            form_instance = form.save(commit=False)

            #additional logic 
            form_instance.contact_person_email = 'default@gmail.com'

            form_instance.save()

            return HttpResponse("<h3>Projects Saved Successfully!!!</h3>")
    else:
        form = ProjectModelForm()
    return render(request, 'addProject.html', {'form': form})


def addEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            #insert data into EMployee table and create the object
            empObj = Employee(first_name=first_name, last_name=last_name, email=email)
            empObj.save()

            #no insert operation just get Department Object
            department = request.POST.get('department')            
            depObj = Department.objects.get(id=department)

            #insert data into EmployeeDetails table and create the object
            designation = request.POST.get('designation')
            about_employee = request.POST.get('about_employee')
            joining_date = request.POST.get('joining_date')
            relieving_date = '9999-09-09'
            birth_date = request.POST.get('birth_date')
            salary = request.POST.get('salary')
            total_experience = request.POST.get('total_experience')

            empDetObj = EmployeeDetails(employee=empObj, department=depObj, designation=designation, about_employee=about_employee, joining_date=joining_date, 
                                        birth_date=birth_date, relieving_date=relieving_date, salary=salary, total_experience=total_experience)
            
            empDetObj.save()

            #get projects object
            projects = request.POST.get('projects')
            projObj = Projects.objects.get(id=projects)

            empDetObj.projects.add(projObj)

            return HttpResponse("<h3>Employee Saved Successfully!!!</h3>")

    else:
        form = EmployeeForm()
    return render(request, 'genericForm.html', {'form': form})


class ListOfProjects(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


@api_view(['POST', 'GET'])
def saveProject(request):
    
    serializer = ProjectsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

