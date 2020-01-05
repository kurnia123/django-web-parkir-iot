from django.urls import path, re_path as url 

from .views import (
	ParkirLIst,
	loginView,
	logoutView,
	updateDBBooking,
	updateDBKosong,
	UseParkir,)

app_name="parkir"
urlpatterns = [
	url(r"^$",ParkirLIst.as_view(),name="list_parkir"),
	url(r'^useparkir/',UseParkir.as_view(),name='useparkir'),
	url(r'^login/',loginView,name='login'),
	url(r'^logout/',logoutView,name='logout'),
	url(r'^updateBooking/(?P<idParkir>[\w]+)$',updateDBBooking,name='update'),
	url(r'^updateKosong/(?P<idParkir>[\w]+)$',updateDBKosong,name='kosong'),
]