from django import forms
from auto_call.models import Patient
from auto_call.models import Room

class  PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ("room", "name", "emergancy", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'اسم المريض'

class  RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name',)