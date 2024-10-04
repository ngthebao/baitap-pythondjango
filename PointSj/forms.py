from django.forms import ModelForm, NumberInput
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import PointSj
from Subject.models import Subject

class PointSjForm(ModelForm):
    pointsj_dcc = forms.FloatField(
        validators=[
            MinValueValidator(1.0), 
            MaxValueValidator(10.0)  
        ],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px; font-size: 12px;', 'min': '1', 'max': '10', 'step': '1'}),
        label= 'Điểm chuyên cần',
    )
    pointsj_exam = forms.FloatField(
        validators=[
            MinValueValidator(1.0),  
            MaxValueValidator(10.0)  
        ],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px; font-size: 12px;', 'min': '1', 'max': '10', 'step': '1'}),
        label='Điểm thi',
    )

    class Meta:
        model = PointSj
        fields = '__all__'
        labels = {
            'student_id': 'Sinh viên',
            'subject_id': 'Môn học',
            'pointsj_dcc': 'Điểm chuyên cần',
            'pointsj_exam': 'Điểm thi',
        }
