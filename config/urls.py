from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', include("profiles.urls"), name='profiles'),
    url('^', include("utsida.urls"), name="index"),
]
