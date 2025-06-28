# core/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def about_us_view(request):
    return render(request, 'aboutUs.html')

def contact_us_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Compose email
            subject = f"Contact Form Submission from {name}"
            full_message = f"Message from {name} <{email}>:\n\n{message}"

            try:
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],  # Send to your email
                    fail_silently=False,
                )
                messages.success(request, "Thank you for contacting us. We'll get back to you soon.")
                return redirect('contact_us')
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'contactUs.html')
