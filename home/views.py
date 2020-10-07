from django.shortcuts import render
from .models import Newsletters
from django.core.mail import send_mail

# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        try:
            cmail = Newsletters.objects.get(email=email)
        except Newsletters.DoesNotExist:
            nletter = Newsletters(
                name=name,
                email=email
            ).save()
            send_mail(
                'Thank You for Subscribing...',
                f'Hey {name},\nThank You for Subscribing to our Blog\'s NewsLetters.\nWe will not let you regret to your decision.\n\tThank You\n\t\tTheHackersBrain [Gaurav Raj]',
                'the4hackersbrain@gmail.com',
                [email],
                fail_silently=False,
            )

    return render(request, 'index.html')
