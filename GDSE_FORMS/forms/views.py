from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils.timezone import now

def home(request):
    return render(request, 'index.html', {'timestamp': now().timestamp()})

def store(request):
    # Retrieving data from GET request (index.html)
    context = {
        'name': request.GET.get("name", ""),
        'email': request.GET.get("email", ""),
        'year': request.GET.get("year", ""),
        'password': request.GET.get("password", ""),
        'gender': request.GET.get("gender", ""),
        'timestamp': now().timestamp(),
    }
    print("Store View Data:", context)  # Debug log
    return render(request, 'base.html', context)

def export(request):
    # Retrieving data from POST request (base.html)
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")  # Correct email retrieval
    year = request.POST.get("year", "")
    password = request.POST.get("password", "")
    gender = request.POST.get("gender", "")

    # Debug print statements
    print(f"Exported Data -> Name: {name}, Email: {email}, Year: {year}, Password: {password}, Gender: {gender}")

    if email:  # Ensure email is not empty before sending
        try:
            # Send email
            send_mail(
                "Confirmation",
                f"Hello {name},\n\nPlease confirm your details:\n\n"
                f"Email: {email}\nYear: {year}\nGender: {gender}\n\n"
                "Thank you!",
                "narentesting1234@gmail.com",  # Sender email
                [email],  # Replace {{email}} with actual email variable
                fail_silently=False,
            )
            return HttpResponse("Done, please check your mail.")
        except Exception as e:
            return HttpResponse(f"Error sending email: {str(e)}")
    else:
        return HttpResponse("Email address is missing!")