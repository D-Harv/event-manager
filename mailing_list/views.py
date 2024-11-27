from django.shortcuts import render, redirect
from .models import Subscriber

def subscribe(request):
    """
    Handles subscription to the mailing list.
    """
    if request.method == "POST":
        email = request.POST.get('email')
        if email and not Subscriber.objects.filter(email=email).exists():
            Subscriber.objects.create(email=email)
            return render(request, 'success.html', {'message': 'You have successfully subscribed!'})
        return render(request, 'subscribe.html', {'error': 'Email is invalid or already subscribed.'})
    return render(request, 'subscribe.html')

def unsubscribe(request):
    """
    Handles unsubscription from the mailing list.
    """
    if request.method == "POST":
        email = request.POST.get('email')
        if email and Subscriber.objects.filter(email=email).exists():
            Subscriber.objects.filter(email=email).delete()
            return render(request, 'success.html', {'message': 'You have successfully unsubscribed!'})
        return render(request, 'unsubscribe.html', {'error': 'Email not found in our mailing list.'})
    return render(request, 'unsubscribe.html')