from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request,'You have sent inquiry about this model. Please wait until we get to you')
                return redirect('/cars/'+car_id)

        contact = Contact(user_id=user_id, car_id=car_id, first_name=first_name, last_name=last_name, customer_need=customer_need, car_title=car_title, city=city, state=state,email=email, phone=phone, message=message)

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email

        send_mail(
            'Car Inquiry',
            message,
            email,
            ['meshlrd14@gmail.com'],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'You request has been submitted. We will get back to you shortly')
        return redirect('/cars/'+car_id)
