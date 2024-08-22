from django.contrib import admin
from patients.models import Biodata
from patients.models import ServiceCategory
from patients.models import Tribes, Service, Drugs, Providedservices
from account.models import User

# Register your models here.
admin.site.register(Biodata)
admin.site.register(User)
admin.site.register(ServiceCategory)
admin.site.register(Tribes)
admin.site.register(Service)
admin.site.register(Drugs)
admin.site.register(Providedservices)
