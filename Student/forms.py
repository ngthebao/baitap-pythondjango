from django.forms import ModelForm
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['std_msv', 'std_name', 'std_year', 'std_address', 'std_gender']
        widgets = {
            'std_msv': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px; font-size: 12px;'}),
            'std_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px; font-size: 12px;'}),
            'std_year': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control datepicker',
                    'placeholder': 'Select a date',
                    'type': 'date',
                    'style': 'width: 300px; height: 30px; font-size: 12px;'
                }
            ),
            'std_address': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px; font-size: 12px;'}),
            'std_gender': forms.Select(
                choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')],
                attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px; font-size: 12px;'}
            ),
        }
        labels = {
            'std_msv': 'Mã sinh viên',
            'std_name': 'Họ và tên',
            'std_address': 'Địa chỉ',
            'std_year': 'Ngày sinh',
            'std_gender': 'Giới tính',
        }