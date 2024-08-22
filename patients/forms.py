from django import forms
from patients.models import Biodata, Tribes, ServiceCategory, Service, Drugcategory, Drugs, Providedservices


class BiodataForm(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = [
            'Firstname', 'Othernames', 'Age', 'weight', 'sex', 'height',
            'tribe', 'Address', 'Phone', 'Emailaddress',
        ]
        widgets = {
            'tribe': forms.Select(attrs={'class': 'form-control'}),
            'sex': forms.Select(choices=[('S','-Select-'), ('M', 'Male'), ('F', 'Female')], attrs={'class': 'form-control'}),
            # Other fields can also be customized with widgets as needed
        }

class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['category']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'service', 'price']
        widgets = {
          'category' : forms.Select(attrs={'class': 'form-control'}),
        }

class drugcategoryForm(forms.ModelForm):
    class Meta:
        model = Drugcategory
        fields = ['category']


class tribeForm(forms.ModelForm):
    class Meta:
        model = Tribes
        fields = ['tribe']
        

class drugForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = ['category', 'name', 'price', 'description']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),

        }



class ProvidedServiceForm(forms.ModelForm):
    class Meta:
        model = Providedservices
        fields = ['category', 'service', 'cost']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'id_category'}),
            'service': forms.Select(attrs={'class': 'form-control', 'id': 'id_service'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            try:
                category_id = self.data.get('category')
                services = Service.objects.filter(category_id=category_id).order_by('service')
                self.fields['service'].queryset = services
            except (ValueError, TypeError):
                self.fields['service'].queryset = Service.objects.none()
        elif self.instance.pk and self.instance.category:
            self.fields['service'].queryset = self.instance.category.service_set.all()
        else:
            self.fields['service'].queryset = Service.objects.none()

