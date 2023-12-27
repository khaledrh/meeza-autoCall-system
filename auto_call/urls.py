from django.urls import path
from auto_call import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="http://127.0.0.1:8000/0/")),
    path("<int:roomid>/", views.HomeListView.as_view() , name="home"),
    path("room/<int:roomid>/", views.PatientListView.as_view(), name="roomlist"),
    path("form/", views.patient_form, name="form"),
    path("delete/<int:roomid>/", views.patient_form_del, name="formdel"),
    path("screen/", views.screen, name="screen"),
    ]