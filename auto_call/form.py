from django import forms
from auto_call.models import Patient
from auto_call.models import Room

class  PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("room", "name",)

class  RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ("name", )