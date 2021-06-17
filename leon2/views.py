from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def appointment(request):
	if request.method == "POST":
		cf_name = request.POST['cf-name']
		cf_email = request.POST['cf-email']
		cf_message = request.POST['cf-message']

		send_mail(

			'You have a new message from: ' + cf_name,
			'Contact info: ' + cf_email + '\n \nNew Message: ' + cf_message,
			cf_message,
			['margaretpedrie@gmail.com'],
			)
		return render(request, 'appointment.html', {})
	else:
		return render(request, 'home.html', {})