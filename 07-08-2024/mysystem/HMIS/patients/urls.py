from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('biodata/', views.biodata, name='biodata'),
    path('addbiodata/', views.addbiodata, name='addbiodata'),
    path('servicecategory/', views.servicecategory, name='servicecategory'),
    path('addservice/', views.addservice, name='addservice'),
    path('getservices/', views.getservices, name='getservices'),
    path('addservicecategory/', views.addservicecategory, name='addservicecategory'),
    path('adddrugcategory/', views.adddrugcategory, name='adddrugcategory'),
    path('getdrugcategory/', views.getdrugcategory, name='getdrugcategory'),
    path('adddrug/', views.adddrug, name='adddrug'),
    path('getdrug/', views.getdrug, name='getdrug'),
    path('tribes/', views.tribes, name='tribes'),
    path('addtribe/', views.addtribe, name='addtribe'),
    path('api/day-counts/', views.day_counts_view, name='day-counts'),
    path('api/tribenames/', views.gettribedropdown, name='tribenames'),
    path('createprovidedservice/', views.createprovidedservice, name='createprovidedservice'),
    path('load_form/', views.load_provided_service_form, name='load_provided_service_form'),
    path('load-services/', views.load_services, name='load_services'),
    path('getprovidedserviceview/', views.getprovidedserviceview, name='getprovidedserviceview'),
    
   

  
    

]