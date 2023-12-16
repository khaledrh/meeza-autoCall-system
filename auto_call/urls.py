from django.urls import path
from auto_call import views

urlpatterns = [
path("<int:roomid>/", views.HomeListView.as_view() , name="home"),
path("room/<int:roomid>/", views.PatientListView.as_view(), name="roomlist"),
path("form/", views.patient_form, name="form"),
path("screen/", views.screen, name="screen"),
]