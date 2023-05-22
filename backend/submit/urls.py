from django.urls import path

from .views import form_submit

urlpatterns = [
    path('', form_submit, name='form_submit'),
]