from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('account.urls')),
    path('',include('patients.urls')),
    path('__reload__/', include('django_browser_reload.urls')),

]
