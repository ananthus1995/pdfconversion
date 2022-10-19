
from .models import Consultation
from .forms import Consult_Form
from django.views.generic import CreateView,ListView,View
from django.urls import reverse_lazy

from io import BytesIO
from django.http import HttpResponse

from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from fileconversion import settings
from time import gmtime, strftime




class Home(CreateView):
    template_name = 'home.html'
    model = Consultation
    form_class = Consult_Form
    success_url = reverse_lazy('all_data')



class All_Data(ListView):
    model = Consultation
    template_name = 'all_data.html'
    context_object_name = 'consult_data'
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')



def fetch_resources(uri, rel):
    path = os.path.join(uri.replace(settings.STATIC_URL, ""))
    return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None




class CreatePdfData(View):
    def get(self, request, *args, **kwargs):
        try:
            consult_data = Consultation.objects.get(id = kwargs.get('con_id'))
        except:
            return HttpResponse("Not Found")
        data = {
            'clinicname': consult_data.clinic_Name,
            'physicnananme': consult_data.pysician_name,
            'physician_number': consult_data.pysician_Contact,
            'patientdob': str(consult_data.patient_dob),
            'patient_fname': consult_data.patient_first_name ,
            'patient_lname': consult_data.patient_last_name,
            'patient_number': consult_data.patient_contact,
            'chiefcomplaint': str(consult_data.chief_complaint),
            'consultnote':consult_data.consultation_note,
            'logo':consult_data.clinic_logo,
            'consult_data':consult_data.created_on,
            'time':strftime("%Y-%m-%d %H:%M:%S", gmtime())

        }

        # print(data)
        pdf = render_to_pdf('result.html', data)
        #return HttpResponse(pdf, content_type='application/pdf')


        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "CR_%s.pdf" %(data['patient_lname']+'_'+data['patient_fname']+'_'+data['patientdob'])
            content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")