from django.shortcuts import render,redirect
from .models import Details
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import requests



# Create your views here.
def verify_email(email):
    import requests

    url = "https://email-checker.p.rapidapi.com/verify/v1"

    querystring = {"email":"name@example.com"}

    headers = {
	    "X-RapidAPI-Key": "1cf271bfa7mshec95cfcdfdbef45p1ef18ejsn6372b6f62902",
	    "X-RapidAPI-Host": "email-checker.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json().get('deliverable', False)
    else:
        return False

    
    
def index(request):
    if request.method == 'POST':
        
        serial_number = request.POST.get('serial_number')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        visit_first_time = request.POST.get('visit_first_time') == 'yes'
        food_you_liked = ', '.join(request.POST.getlist('food_you_liked'))
        time_slot = request.POST.get('time_slot')
        upload_photo = request.FILES.get('upload_photo')

        # validation
        errors = {}
        
        
        if len(phone_number) != 10 or not phone_number.isdigit():
            errors['phone_number'] = 'Invalid phone number'
        try:
            validate_email(email)
        except ValidationError:
            errors['email'] = 'Invalid email address'

        if not verify_email(email):
            errors['email'] = 'Email address is not deliverable'

        if errors:
            return render(request, "index.html", {'errors': errors})
    

        details = Details(
            serial_number=serial_number,
            Name=name,
            Phone_number=phone_number,
            Email=email,
            Visit_First_Time=visit_first_time,
            Food_You_liked=food_you_liked,
            Time_slot=time_slot,
            Upload_Photo=upload_photo
        )
        details.save()
        return redirect('index')  

    return render(request, "index.html")


def AllFeedback(request):
    feedback = Details.objects.all()
    search_query = request.GET.get('search')
    food_query = request.GET.get('food')
    if search_query:
        feedback = feedback.filter(Name=search_query)
    if food_query:
        feedback = feedback.filter(Food_You_liked=food_query)
    return render(request, 'allFeedback.html', {'feedback': feedback})