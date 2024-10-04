from django.shortcuts import render, redirect
from .models import PointSj as pointsj_model
from Subject.models import Subject as subject_model
from Student.models import Student as student_model
from .forms import PointSjForm
from Subject.views import get_subject
import pandas as pd

# Create your views here.
def get_pointsj(request, id):
    pointsj_list = pointsj_model.objects.filter(subject_id = id) 
    subject = subject_model.objects.get(subject_id = id)
    return render(request, 'pointsj.html', {'pointsj_list': pointsj_list, 'subject' : subject})


def addPoint(request):
    form = PointSjForm()
    if request.method == 'POST':
        form = PointSjForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject_id']
            s = subject.subject_id
            form.save()
            return redirect('/point/' + str(s))
    context = {'form': form}
    return render(request, 'add_point.html', context)

def editPointsj(request, pk):
    student = pointsj_model.objects.get(student_id =pk)
    form = PointSjForm(instance=student)
    if request.method == "POST":
        form = PointSjForm(request.POST, instance=student)
        if form.is_valid():
            subject = form.cleaned_data['subject_id']
            s = subject.subject_id
            form.save()
            return redirect('/point/' + str(s))
    context = {'form':form}
    return render(request, 'edit_pointsj.html', context)

def deletePointsj(request, pk):
    student_data = pointsj_model.objects.get(student_id=pk)
    subject = student_data.subject_id
    s = subject.subject_id
    student_data.delete()
    return redirect('/point/' + str(s))

def upload_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        if excel_file.name.endswith('.xlsx'):
            df = pd.read_excel(excel_file, header=0)
            for index, row in df.iterrows():
                student_id, _ = student_model.objects.get_or_create(
                    std_msv=row['Mã sinh viên'],
                    defaults={'std_name': row['Tên sinh viên']}
                )
                subject_id, _ = subject_model.objects.get_or_create(
                    subject_msj=row['Mã Môn Học'] 
                )
                pointsj_model.objects.update_or_create(
                    student_id=student_id,
                    subject_id=subject_id,
                    defaults={
                        'pointsj_dcc': row['Điểm chuyên cần'],
                        'pointsj_exam': row['Điểm thi']
                    }
                )
            return redirect(get_subject)
        else:
            return render(request, 'upload_excel.html', {'error': 'File không đúng định dạng'})
    else:
        students = student_model.objects.all()
        return render(request, 'upload_excel.html', {'students': students})
    
def searchPointsjStudent(request, id):
    if 'query' in request.GET:
        query = request.GET.get('query')
        pointsj_list = pointsj_model.objects.filter(student_id__std_name__icontains=query).order_by('student_id__std_name')
        subject = subject_model.objects.get(subject_id = id)
        return render(request, 'pointsj.html', {'pointsj_list': pointsj_list , 'subject' : subject})
    else:
        return render(request, 'pointsj.html', {'pointsj_list': [] , 'subject' : []})


