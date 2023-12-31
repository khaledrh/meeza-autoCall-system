from django.urls import path
from auto_call import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/0/")),
    path("<int:roomid>/", views.HomeListView.as_view() , name="home"),
    path("room/<int:roomid>/", views.PatientListView.as_view(), name="roomlist"),
    path("form/", views.patient_form, name="form"),
    path("delete/<int:roomid>/", views.patient_form_del, name="formdel"),
    path("screen/", views.slideshow, name="screen"),
    path('slideshow/', views.slideshow, name='slideshow'),

    ]