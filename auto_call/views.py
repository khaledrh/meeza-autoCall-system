from django.shortcuts import render
from django.views.generic import ListView
from auto_call.models import Patient
from auto_call.form import PatientForm
from auto_call.models import Room
from auto_call.form import RoomForm
from django.utils.timezone import datetime
from django.shortcuts import redirect


class HomeListView(ListView):
    model = Patient

    def get_context_data(self, **kwargs):
        return super(HomeListView, self).get_context_data(**kwargs)
    
def screen(request):
    return render(request, "auto_call/screen.html")


def patient_form(request):
    form = PatientForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("screen")
    else:
        return render(request, "auto_call/patient_form.html", {"form": form})

def room_form(request):
    form = RoomForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("screen")
    else:
        return render(request, "auto_call/room_form.html", {"form": form})