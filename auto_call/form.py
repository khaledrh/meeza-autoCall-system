from django import forms
from auto_call.models import Patient
from auto_call.models import Room

class  PatientForm(forms.ModelForm):
    # patient_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # room = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Patient
        fields = ("room", "name", "emergancy", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].empty_label = 'الغرفه'
        # self.fields['room'].label = ''
        # self.fields['room'].widget.attrs.update({'class': 'room-input'})
        # self.fields['name'].label = ''
        # self.fields['name'].widget.attrs.update({'class': 'name-input', 'placeholder': f'اسم المريض'})
        # self.fields['emergancy'].label = 'طوارئ'
        # self.fields['emergancy'].widget.attrs.update({'class': 'emrg-input'})
        

class  RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']