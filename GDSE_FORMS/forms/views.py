from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils.timezone import now

def home(request):
    return render(request, 'index.html', {'timestamp': now().timestamp()})

def store(request):
    # Retrieving data from GET request
    name = request.GET.get("name", "")
    email = request.GET.get("email", "")
    year = request.GET.get("year", "")
    password = request.GET.get("password", "")
    gender = request.GET.get("gender", "")
    final = request.GET.get("final", "")
    
    # Debug print statements
    print(name, email, year, password, gender, final)
    
    # Combining data into a single context dictionary
    context = {
        'name': name,
        'email': email,
        'year': year,
        'password': password,
        'gender': gender,
        'final': final,
        'timestamp': now().timestamp()
    }
    
    return render(request, 'base.html', context)

def export(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    year = request.POST.get("year", "")
    password = request.POST.get("password", "")
    gender = request.POST.get("gender", "")
    final = request.POST.get("final", "")
    
    # Debug print statements
    print(name, email, year, password, gender, final)
    
    # Send email
    send_mail(
        "Confirmation",
        f"Hello, please confirm your details. Here is your name: {name}",
        "narentesting1234@gmail.com",
        ["snarenkumar30@gmail.com"],  # Email passed here directly
        fail_silently=False,
    )
    
    return HttpResponse("Done, please check your mail.")