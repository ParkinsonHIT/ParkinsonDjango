from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Doctor, Patient

import os


class RegisterForm(UserCreationForm):  # django registration form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'סיסמא'
        self.fields['password2'].label = 'אישור סיסמא'
        self.fields[
            'password1'].help_text = "<li>הסיסמה שלך לא יכולה להיות דומה מדי למידע האישי האחר שלך.</li>" \
                                     "<li>הסיסמה שלך חייבת להכיל לפחות 8 תווים.</li>" \
                                     "<li>הסיסמה שלך לא יכולה להיות סיסמה נפוצה.</li>" \
                                     "<li>הסיסמה שלך חייבת להכיל אותיות ומספרים לחלוטין.</li>"
        self.fields['password2'].help_text = '<li>אנא הזן סיסמא בשנית.</li>'

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "first_name", "last_name")
        labels = {
            "email": "אימייל",
            "first_name": "שם פרטי",
            "last_name": "שם משפחה"
        }
        attrs = {
            'dir': 'rtl',
        }


class DoctorRegisterForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('זכר', 'זכר'),
        ('נקבה', 'נקבה')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="מין")

    class Meta:
        model = Doctor
        fields = ("gender", "office_phone", "mobile_phone", "organization")
        exclude = ('user',)  # this should be removed


class DateInput(forms.DateInput):
    input_type = 'date'


class PatientRegisterForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('זכר', 'זכר'),
        ('נקבה', 'נקבה')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="מין")
    date_of_birth = forms.DateField(widget=DateInput, label="תאריך לידה")

    class Meta:
        model = Patient
        fields = "__all__"
