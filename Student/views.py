from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student as student_model
from .forms import StudentForm
import pandas as pd


# Create your views here.
def get_std(request):
    student_list = student_model.objects.filter().order_by()
    return render(request,'student.html', {'student_list': student_list})

def addStudent(request):
    form = StudentForm
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm thành công!')
            return redirect(get_std)
    context = {'form':form}
    return render(request, 'add_student.html', context)

def editStudent(request, pk):
    std_id = student_model.objects.get(std_id=pk)
    form = StudentForm(instance=std_id)
    
    if request.method == "POST":
        form = StudentForm(request.POST, instance=std_id)
        if form.is_valid():
            form.save()
            return redirect(get_std)
    context = {'form':form}
    return render(request, 'edit_student.html', context)

def deleteStudent(request, pk):
    student_data = student_model.objects.get(std_id=pk)
    student_data.delete()
    return redirect(get_std)

def searchStudentName(request):
    if 'query' in request.GET:
        query = request.GET.get('query')
        student_list = student_model.objects.filter(std_name__icontains=query).order_by('std_name')
        return render(request, 'student.html', {'student_list': student_list})
    else:
        return render(request, 'student.html', {'student_list': []})
    



def upload_excel_student(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        if excel_file.name.endswith('.xlsx'):
            df = pd.read_excel(excel_file, header=0)
            for index, row in df.iterrows():
                student_id, _ = student_model.objects.get_or_create(
                    std_msv=row['Mã sinh viên'],
                    defaults={
                        'std_name': row['Tên sinh viên'],
                        'std_year': row['Năm sinh'],
                        'std_address': row['Địa chỉ'],
                        'std_gender': row['Giới tính'],
                    }
                )
            return redirect(get_std)
        else:
            return render(request, 'upload_excel_std.html', {'error': 'File không đúng định dạng'})
    else:
        students = student_model.objects.all()
        return render(request, 'upload_excel_std.html', {'students': students})