from django import forms
from .models import Consultation
import re
class Consult_Form(forms.ModelForm):


    class Meta:
        model= Consultation
        fields = ['clinic_Name','clinic_logo','pysician_name','pysician_Contact','patient_first_name','patient_last_name','patient_dob','patient_contact','chief_complaint','consultation_note']
        widgets = {

            'clinic_Name': forms.TextInput(attrs={'class': 'form-control','placeholder':'clinic Name'}),
            'clinic_logo': forms.FileInput(attrs={'class': "  form-control",'placeholder':'clinic logo'}),
            'pysician_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'physician Name'}),
            'pysician_Contact': forms.TextInput(attrs={'class': 'form-control','placeholder':'physician contact'}),
            'patient_first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'patient first name'}),
            'patient_last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'patient last name'}),
            'patient_dob': forms.DateInput(attrs={'class': 'form-control ', 'type': 'date'}),
            'patient_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'patient contact'}),
}

    def clean(self):
            cleaned_data = super().clean()
            pysician_number = cleaned_data.get('pysician_Contact')
            patient_number = cleaned_data.get('patient_contact')
            pysician_name = cleaned_data.get('pysician_name')
            patient_fname=cleaned_data.get('patient_first_name')

            if len(pysician_name) < 4:
                self.add_error('pysician_name', 'Minimum 4 letters needed')

            if len(patient_fname) < 4:
                self.add_error('patient_first_name', 'Minimum 4 letters needed')


            if pysician_number:

                rule = '[0-9]{10}'
                match = re.fullmatch(rule, pysician_number)
                if match is None:
                    self.add_error('pysician_Contact', 'Mobile number must be contain 10digits')

            if patient_number:

                rule = '[0-9]{10}'
                match = re.fullmatch(rule, patient_number)
                if match is None:
                    self.add_error('patient_contact', 'Mobile number must be contain 10digits')

            if pysician_number == patient_number:
                self.add_error('patient_contact', 'same as Physician Number.should use different mobilenumber')
                self.add_error('pysician_Contact', 'same as Patient Number.should use different mobilenumber')
