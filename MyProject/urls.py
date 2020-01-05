from django.contrib import admin
from django.urls import path, include, re_path as url

from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='home'),   
    url(r'^parkir/',include('parkir.urls',namespace='parkir')),
]
