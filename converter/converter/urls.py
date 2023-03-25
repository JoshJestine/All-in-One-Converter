from django.urls import path
from content import views

app_name = 'content'

urlpatterns = [    path('', views.home),    path('pdf_to_docx/', views.pdf_to_docx),]