from django.urls import path
from . import views


urlpatterns = [
    path('add_department/', views.addDepartment, name='add_department'),
    path('add_project/', views.addProject, name='add_project'),
    path('add_employee/', views.addEmployee, name='add_employee'),
    path('all_projects/', views.ListOfProjects.as_view(), name='all_projects'),
    path('save_project/', views.saveProject, name='save_project')
]