"""
URL configuration for QuanLySV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views as app
from PointSj import views as Pointsj
from Student import views as Student
from Subject import views as Subject



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.get_home),
    # Danh sách các trang chính
    path('subject/', Subject.get_subject),
    path('student/', Student.get_std),
    path('point/<int:id>/', Pointsj.get_pointsj, name = "point"),
    # Các chức năng của student
    path('add-student/', Student.addStudent, name='addStudent'),
    path('edit-student/<int:pk>/', Student.editStudent, name="edit-student"),
    path('delete-student/<str:pk>/', Student.deleteStudent, name="delete-student"),
    path('searchstudent/', Student.searchStudentName, name='search_student_by_name'),
    path('updatestd/', Student.upload_excel_student, name="upload-excel-std"),
    # Các chức năng của subject
    path('add-subject/', Subject.addSubject, name='addSubject'),
    path('edit-subject/<str:pk>/', Subject.editSubject, name="edit-subject"),
    path('delete-subject/<str:pk>/', Subject.deleteSubject, name="delete-subject"),
    path('searchsubject/', Subject.searchSubjectByName, name='search_subject_by_name'),
    # Chức năng của pointsj
    path('addPoint/', Pointsj.addPoint, name='addPoint'),
    path('delete-pointsj/<str:pk>/', Pointsj.deletePointsj, name="delete-pointsj"),
    path('edit-pointsj/<str:pk>/', Pointsj.editPointsj, name="edit-pointsj"),
    path('update/', Pointsj.upload_excel, name="upload-excel"),
    path('searchpointsj/<int:id>/', Pointsj.searchPointsjStudent, name='search_pointsj_by_name'),
]