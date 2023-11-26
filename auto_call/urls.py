from django.urls import path
from auto_call import views
from auto_call.models import Patient

home_list_view = views.HomeListView.as_view(
    queryset=Patient.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="autocall/screen.html"
)

urlpatterns = [
path("", home_list_view, name="home"),
path("form/", views.patient_form, name="form"),
path("roomform/", views.room_form, name="room"),
path("screen/", views.screen, name="screen")
]