from django.shortcuts import render
from django.http import JsonResponse


def form_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name)
        # Process the form data as required
        # ...

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Form data submitted successfully.'})

