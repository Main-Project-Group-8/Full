from django.shortcuts import render
from django.http import JsonResponse

def submit_form(request):
    
    if request.method == 'POST':
        form_data = request.POST
        name = form_data.get('name')
        email = form_data.get('email')
        message = form_data.get('message')
        
        return JsonResponse({'message': 'Form submitted successfully'})
