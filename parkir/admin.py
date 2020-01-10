from django.contrib import admin
from .models import *

# Register your models here.

class tempatParkirAdmin(admin.ModelAdmin):
	readonly_fields = [
		'user',
	]

admin.site.register(OnParkir)
admin.site.register(Booking)
admin.site.register(tempatParkir,tempatParkirAdmin)