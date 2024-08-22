from itertools import count
from django.shortcuts import render
from .models import Biodata
from .models import ServiceCategory, Service, Drugcategory, Drugs
from .models import Tribes
from django.http import JsonResponse
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BiodataForm
from .forms import ServiceCategoryForm, ServiceForm, drugcategoryForm, drugForm, tribeForm
from .models import Providedservices
from .forms import ProvidedServiceForm
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def biodata(request):

    context = {
        'Biodatas': Biodata.objects.all()  # This will be available for both GET and POST requests
    }
        # Update context with the latest Biodata records
    day_counts = Biodata.objects.values('day_of_week').annotate(count=Count('id')).order_by('day_of_week')
    context['day_counts'] = list(day_counts)
    context['Biodatas'] = Biodata.objects.all()

    return render(request, 'patients/biodata.html', context)

@login_required
def day_counts_view(request):
    day_counts = Biodata.objects.values('day_of_week').annotate(count=Count('id')).order_by('day_of_week')
    return JsonResponse(list(day_counts), safe=False)

@login_required
def addbiodata(request):
    if request.method == 'POST':
        form = BiodataForm(request.POST)
        if form.is_valid():
            formtosave = form.save(commit=False)
            formtosave.added_by = request.user
            formtosave.save()
            return redirect('patients:biodata')  
    else:
        form = BiodataForm()
    
    return render(request, 'patients/addbiodata.html', {'form': form})

@login_required
def addservicecategory(request):
    if request.method == 'POST':
        form = ServiceCategoryForm(request.POST)
        if form.is_valid():
            formtosave = form.save(commit=False)
            formtosave.added_by = request.user
            formtosave.save()
            return redirect('patients:servicecategory') 
    else:
        form = ServiceCategoryForm()

    return render(request, 'patients/addservicecategory.html', {'form': form})



from django.shortcuts import render
from .models import ServiceCategory



@login_required
def servicecategory(request):
    context = {
        'categories': ServiceCategory.objects.all()  # Use a consistent and appropriate key name
    }
    return render(request, 'patients/servicecategory.html', context)

@login_required
def tribes(request):

    context = {
        'tribes' : Tribes.objects.all()
    }

    return render(request, 'patients/tribes.html', context)



@login_required    
def addtribe(request):
    if request.method == 'POST':
        form = tribeForm(request.POST)
        if form.is_valid():
            formtosave = form.save(commit=False)
            formtosave.added_by = request.user
            formtosave.save()
            messages.success(request, 'Tribe added successfully!')
            return redirect('patients:tribes')  # Adjust URL name as necessary
        else:
            messages.error(request, 'Please correct the errors below.')
            print(form.errors)  # For debugging
    else:
        form = tribeForm()

    return render(request, 'patients/addtribe.html', {'form': form})
@login_required
def addservice(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            formtosave = form.save(commit=False)
            formtosave.added_by = request.user
            formtosave.save()
            return redirect('patients:getservices') 
    else:
        form = ServiceForm()

    return render(request, 'patients/addservice.html', {'form': form})

@login_required
def getservices(request):

    context = {
        'services' : Service.objects.all()
    }

    return render(request, 'patients/Services.html', context)

@login_required
def adddrugcategory(request):
    if request.method == 'POST':
        form = drugcategoryForm(request.POST)
        if form.is_valid():
            formtosave = form.save(commit=False)
            formtosave.added_by = request.user
            formtosave.save()
            return redirect('patients:getdrugcategory') 
    else:
        form = drugcategoryForm()

    return render(request, 'patients/adddrugcategory.html', {'form': form})

@login_required
def getdrugcategory(request):

    context = {
        'categories' : Drugcategory.objects.all()
    }

    return render(request, 'patients/drugcategory.html', context)
@login_required
def adddrug(request):
    if request.method == 'POST':
        form = drugForm(request.POST)
        if form.is_valid():
            formtosave = form.save(commit=False)
            formtosave.added_by = request.user
            formtosave.save()
            return redirect('patients:getdrug')
        else:
            print(form.errors)  # This line prints the form errors to the console
    else:
        form = drugForm()

    return render(request, 'patients/adddrug.html', {'form': form})


def getdrug(request):

    context = {
        'drugs' : Drugs.objects.all()
    }

    return render(request, 'patients/drug.html', context)

@login_required
def createprovidedservice(request):
    if request.method == 'POST':
        form = ProvidedServiceForm(request.POST)
        if form.is_valid():
            # Print individual values
            print("Form data:", request.POST)
            patient_id = request.POST.get('patient_id')
            category_id = request.POST.get('category')
            service_id = request.POST.get('service')



            provided_service = form.save(commit=False)
            try:
                patient = Biodata.objects.get(id=patient_id)
                provided_service.patient = patient
                provided_service.added_by = request.user
                provided_service.save()

                # Save patient_id in session
                request.session['patient_id'] = patient_id

                return redirect('patients:getprovidedserviceviewbyPatientId') 
            except Biodata.DoesNotExist:
                form.add_error(None, "Patient does not exist.")
    else:
        form = ProvidedServiceForm()

    return render(request, 'patients/providedservice.html', {'form': form})



@login_required
def load_provided_service_form(request):
    if request.method == 'GET':
        form = ProvidedServiceForm()
        html = render_to_string('patients/providedservice.html', {'form': form}, request=request)
        return JsonResponse({'html': html})
    



@login_required
def getprovidedserviceview(request):
    # Fetch all patients with their provided services and related services
    patients_with_services = Biodata.objects.prefetch_related('providedservices_set__service').all()
    
    context = {
        'patients_with_services': patients_with_services,
    }
    
    # For debugging, print the data to the console
    for patient in patients_with_services:
        print(f"Patient: {patient.Firstname} {patient.Othernames}")
        for provided_service in patient.providedservices_set.all():
            print(f"  Service: {provided_service.service.created_at}, Price: {provided_service.service}")
    
    return render(request, 'patients/patientsandservices.html', context)


# @login_required
# def getprovidedserviceviewbyPatientId(request):
#     # Get the patient ID from the session
#     patient_id = request.session.get('patient_id')
#     # Get the patient ID from the request query parameters
#     patient_id = request.GET.get('patient_id')  # Use request.POST.get() for POST requests
#     # Filter the Biodata objects based on the patient ID
#     patients_with_services = Biodata.objects.filter(id=patient_id).prefetch_related('providedservices_set__service')

#     context = {
#         'patients_with_services': patients_with_services,
#     }

#     # For debugging, print the data to the console
#     for patient in patients_with_services:
#         print(f"Patient: {patient.Firstname} {patient.Othernames}")
#         for provided_service in patient.providedservices_set.all():
#             print(f"  Service: {provided_service.service.created_at}, Price: {provided_service.service}")

#     return render(request, 'patients/servicerecipt.html', context)



def getprovidedserviceviewbyPatientId(request):
    # Get the patient ID from the session or query parameters
    patient_id = request.session.get('patient_id') or request.GET.get('patient_id')
    
    # Filter the Biodata objects based on the patient ID
    patients_with_services = Biodata.objects.filter(id=patient_id).prefetch_related('providedservices_set__service')

    # Print the retrieved data to the terminal
    for patient in patients_with_services:
        print(f"Patient: {patient.Firstname} {patient.Othernames}, Age: {patient.Age}, Weight: {patient.weight}")
        for provided_service in patient.providedservices_set.all():
            print(f"  Service: {provided_service.service.service}, Date: {provided_service.service.created_at}, Amount: {provided_service.service.price}")

    context = {
        'patients_with_services': patients_with_services,
    }

    return render(request, 'patients/servicerecipt.html', context)



#gettribesjasonfile
@login_required
def load_services(request):
    category_id = request.GET.get('category_id')
    services = Service.objects.filter(category_id=category_id).order_by('service')
    return JsonResponse({'services': list(services.values('id', 'service'))})
@login_required
def gettribedropdown(request):
    tribeName = Tribes.objects.values('id', 'tribe').order_by('tribe')
    return JsonResponse(list(tribeName), safe=False)


# @login_required
def servicerecipt(request):
    return render(request, 'patients/servicerecipt.html')