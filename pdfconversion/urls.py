from django.urls import path
from pdfconversion import views

urlpatterns=[
    path('', views.Home.as_view(),name='home'),
    path('all_details',views.All_Data.as_view(),name='all_data'),
    path('pdf/<int:con_id>', views.CreatePdfData.as_view(), name='user_pdf_view'),

]