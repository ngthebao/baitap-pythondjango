from django.shortcuts import render, redirect
from .models import Subject as subject_model
from .forms import SubjectForm

# Create your views here.

def get_subject(request):
    subject_list = subject_model.objects.filter().order_by('subject_msj')
    return render(request,'subject.html', {'subject_list': subject_list})

def addSubject(request):
    form = SubjectForm
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(get_subject)
    context = {'form':form}
    return render(request, 'add_subject.html', context)

def editSubject(request, pk):
    subject_msj = subject_model.objects.get(subject_msj=pk)
    form = SubjectForm(instance=subject_msj)
    
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject_msj)
        if form.is_valid():
            form.save()
            return redirect(get_subject)
    context = {'form':form}
    return render(request, 'edit_subject.html', context)

def deleteSubject(request, pk):
    subject_data = subject_model.objects.get(subject_id=pk)
    subject_data.delete()
    return redirect(get_subject)

def searchSubjectByName(request):
    if 'query' in request.GET:
        query = request.GET.get('query')
        subject_list = subject_model.objects.filter(subject_name__icontains=query).order_by('subject_name')
        return render(request, 'subject.html', {'subject_list': subject_list})
    else:
        return render(request, 'subject.html', {'subject_list': []})
