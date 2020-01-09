from django.shortcuts import render,redirect
from django.views.generic import ListView,UpdateView,TemplateView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers

from .models import tempatParkir,Booking,OnParkir
from .forms import BookingForm
import random
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings


class ParkirLIst(LoginRequiredMixin,ListView):
	model = tempatParkir
	template_name = "parkir/parkir_list.html"
	context_object_name = 'parkir_list'
	# Login Required
	login_url = '/parkir/login/'
	redirect_field_name = 'redirect_to'

	def get_queryset(self):
		self.queryset = self.model.objects.filter(status='kosong')
		return super().get_queryset()


class UseParkir(LoginRequiredMixin,ListView):
	model = tempatParkir
	template_name = "parkir/use_parkir.html"
	context_object_name = 'use_parkir'
	# Login Required
	login_url = '/parkir/login/'
	redirect_field_name = 'redirect_to'

	def get_queryset(self):
		user = User.objects.get(username=self.request.user)
		self.queryset = self.model.objects.filter(status='booking',user=user)
		return super().get_queryset()


def updateDBBooking(request,idParkir):
	try:
		user = User.objects.get(username=request.user)
		data = tempatParkir.objects.get(id_parkir=idParkir)
		data.status = 'booking'
		data.user = user

		data.save()
	except Exception as e:
		return redirect("/parkir/")


	return redirect("/parkir/useparkir/")


def updateDBKosong(request,idParkir):
	user = User.objects.get(username=request.user)
	data = tempatParkir.objects.get(id_parkir=idParkir)
	data.status = 'kosong'
	data.user = None
	data.save()

	databooking = Booking.objects.get(booking=data.booking.pk)
	databooking.delete()
	return redirect("/parkir/")


def loginView(request):
	model = User.objects.all()
	context = {
		'page_title':'LOGIN',
		'user':model,
	}

	user = None
	if request.method == "POST":
		username_login = request.POST['username']
		password_login = request.POST['password']

		user = authenticate(request,username=username_login,password=password_login)

		if user is not None:
			login(request,user)
			return redirect('/parkir/')
		else:
			return redirect('/parkir/login/')

	return render(request, 'parkir/login.html',context)


def logoutView(request):
	logout(request)	
	return redirect("/parkir/login/")


def booking_view(request,idParkir):
	booking_view = BookingForm(request.POST or None)

	value = str(random.randint(1000,9999))
	idbooking = "BO" + value
	data = tempatParkir.objects.get(id_parkir=idParkir)

	context = {
		'parkir':idParkir,
		'id_booking':idbooking,
		'formpinjam_senjata':booking_view,
	}

	if request.method == 'POST':
		if booking_view.is_valid():
			try:
				user = User.objects.get(username=request.user)
				data = tempatParkir.objects.get(id_parkir=idParkir)
				data.status = 'booking'
				data.user = user

				data.save()
			except Exception as e:
				return redirect("/parkir/")
			booking_view.save()
			return redirect("/parkir/useparkir/")
	return render(request,'parkir/booking_view.html',context)
	


def onParkir(request):
	value = str(random.randint(1000,9999))
	idonparkir = "OP" + value

	if request.method == "POST":
		kode_booking = request.POST['onparkir']
		try:
			data = Booking.objects.get(booking=kode_booking)
			OnParkir.objects.create(
				id_on_parkir = idonparkir,
				position = kode_booking.parkir.position,
				delayposition = kode_booking.parkir.delayposition,
				)
		except Exception as e:
			return redirect("/parkir/onparkir/")

	return render(request,'parkir/onparkir.html')


def jsonData(request):
	
	data = OnParkir.objects.all()

	raw_json = {
		'position': data.,
		'delayposition':,
	}