from django.urls import path, re_path as url 

from .views import (
	ParkirLIst,
	loginView,
	logoutView,
	updateDBBooking,
	updateDBKosong,
	booking_view,
	UseParkir,
	onParkir,
	jsonData,
	delete_onparkir,)

app_name="parkir"
urlpatterns = [
	url(r"^$",ParkirLIst.as_view(),name="list_parkir"),
	url(r'^useparkir/',UseParkir.as_view(),name='useparkir'),
	url(r'^login/',loginView,name='login'),
	url(r'^logout/',logoutView,name='logout'),
	url(r'^updateBooking/(?P<idParkir>[\w]+)$',updateDBBooking,name='update'),
	url(r'^updateKosong/(?P<idParkir>[\w]+)$',updateDBKosong,name='kosong'),
	url(r'^bookingview/(?P<idParkir>[\w]+)$',booking_view,name='booking'),
	url(r'^onparkir/$',onParkir,name='onparkir'),
	url(r'^jsondata/$',jsonData,name='jsondata'),
	url(r'^deleteonparkir$',delete_onparkir,name='delete_on_parkir'),
]