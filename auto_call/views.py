from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from auto_call.models import Patient
from auto_call.form import PatientForm
from auto_call.form import RoomForm
from django.utils.timezone import datetime
from django.shortcuts import redirect


class HomeListView(ListView):
    model = Patient
    
    # queryset=Patient.objects.order_by("-log_date")[:5],
    # context_object_name="message_list",
    # template_name="auto_call/patient_list.html"

    def get_context_data(self, **kwargs):
        return super(HomeListView, self).get_context_data(**kwargs)
        

class PatientListView(ListView):
    model = Patient
    context_object_name ="patient_list"
    template_name="auto_call/patient_in_waiting.html"
    
    def get_queryset(self):
        return Patient.objects.order_by("log_date").filter(room = self.kwargs["roomid"])[:5]
    
    # def get_context_data(self, **kwargs): 
    #     context = super().get_context_data(**kwargs)
    #     return context
    


# def room_list(request, room_num):
#     roomlist = Patient.objects.filter(room__pk = room_num)[:5]
#     # .order_by( "emergancy", "log_date")
#     return render(request, "auto_call/patient_in_waiting.html", )

    
# def room_list(request, roomnum):
#     room = Patient.objects.filter(roomnum = roomnum)
#     patients_waiting = room.name.all()
#     return render(request, 'room_patients.html', {'room': room, 'patients_waiting': patients_waiting})


def screen(request):
    return render(request, "auto_call/screen.html")


def patient_form(request):
    form = PatientForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("form")
    else:
        return render(request, "auto_call/patient_form.html", {"form": form})

def room_form(request):
    form = RoomForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("room")
    else:
        return render(request, "auto_call/room_form.html", {"form": form})