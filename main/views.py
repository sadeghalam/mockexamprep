from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import UserRegistration, ContactMessage

def home(request):
    return render(request, 'home.html')

def practice(request):
    return render(request, 'practice.html')

def examiners(request):
    return render(request, 'examiners.html')

def services(request):
    return render(request, 'services.html')

def learn_more(request):
    return render(request, 'learn_more.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if password == confirm_password:
            # In production, hash the password using Django's authentication system
            user = UserRegistration(name=name, email=email, password=password)
            user.save()
            return redirect('signup_success')  # Redirect to a success page
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
    return render(request, 'signup.html')

def signup_success(request):
    return render(request, 'signup_success.html')

def about(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = ContactMessage(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )
        contact.save()
        return redirect('contact_success')
    return render(request, 'about.html')

def contact_success(request):
    return render(request, 'contact_success.html')

def book(request):
    return render(request, 'book.html')


def booking_confirmation(request):
    event_type_name = request.GET.get('event_type_name', 'Mock Exam')
    invitee_name = request.GET.get('invitee_full_name', 'Guest')
    return render(request, 'booking_confirmation.html', {
        'event_type_name': event_type_name,
        'invitee_name': invitee_name
    })