from django.db import models
from ckeditor.fields import RichTextField



class Consultation(models.Model):
    clinic_Name=models.CharField(max_length=100)
    clinic_logo= models.ImageField(upload_to='clinic_logo')
    pysician_name= models.CharField(max_length=80)
    pysician_Contact = models.CharField(max_length=80)
    patient_first_name= models.CharField(max_length=80)
    patient_last_name = models.CharField(max_length=80)
    patient_dob= models.DateField(null=True, auto_now=False, auto_now_add=False)
    patient_contact= models.CharField(max_length=50)
    chief_complaint=RichTextField()
    consultation_note = RichTextField()
    created_on=models.DateTimeField(auto_now_add=True)


    def getfullname(self):
        return self.patient_first_name+" "+self.patient_last_name




