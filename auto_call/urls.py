from django.urls import path
from auto_call import views
from auto_call.models import Patient

home_list_view = views.HomeListView.as_view(
    queryset=Patient.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="auto_call/patient_list.html"
)

# patient_list_view = views.PatientListView.as_view(
#     queryset = Patient.objects.order_by( "emergancy", "log_date"),
#     # .filter(room__pk = room_num)[:5],
#     context_object_name = "patient_list",
#     template_name="autocall/patient_in_waiting.html"
# )

urlpatterns = [
path("", home_list_view , name="home"),
path("<int:roomid>/", views.PatientListView.as_view(), name="roomlist"),
path("form/", views.patient_form, name="form"),
path("roomform/", views.room_form, name="room"),
path("screen/", views.screen, name="screen"),
# path("patientbyroom/<int:class>/", views.room_list, name="roomlist"),
]
