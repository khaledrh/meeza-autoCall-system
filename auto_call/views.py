from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from auto_call.models import Patient, Room
from auto_call.form import PatientForm
from django.utils.timezone import datetime
from django.shortcuts import redirect


class HomeListView(ListView):
    model = Patient
    context_object_name="message_list"
    template_name="auto_call/patient_list.html"

    def get_queryset(self):
        room = self.kwargs["roomid"]
        if room == 0:
            return Patient.objects.order_by("-emergancy","log_date")
        else:
            return Patient.objects.order_by("-emergancy","log_date").filter(room = self.kwargs["roomid"])
        

class PatientListView(ListView):
    model = Patient
    context_object_name ="patient_list"
    template_name="auto_call/patient_in_waiting.html"
    
    def get_queryset(self):
        return Patient.objects.order_by("-emergancy","log_date").filter(room = self.kwargs["roomid"])[:5]


def screen(request):
    return render(request, "auto_call/screen.html")

def patient_form(request):
    form = PatientForm(request.POST or None)
    rooms = Room.objects.all()

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            # message.room = 
            room = request.POST.get('room')
            room = Room.objects.get(pk=room)
            message.room = room
            message.log_date = datetime.now()
            message.save()
            return redirect("form")
    else:
        return render(request, "auto_call/patient_form.html", {"form": form , "rooms": rooms})
    

def patient_form_del(request, roomid):
    if request.method == "POST":
        # Retrieve the patient based on roomid
        patient = get_object_or_404(Patient, room=roomid)
        
        # Delete the patient
        patient.delete()
        
        # Redirect to a suitable URL after deletion (You can change this as per your requirement)
        return redirect("home")
    else:
        # Handle the case where the user accesses the URL without a POST request
        return "Bad Request"