from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail

# Declare global variables at the top of the file
global_data = {
    "name": "",
    "email": "",
    "year": "",
    "password": "",
    "gender": "",
    "final": ""
}


from django.core.mail import send_mail

def store(request):
    global global_data  # Declare global to modify the variable inside this function
    
    # Retrieve data from GET request
    global_data["name"] = request.GET.get("name", "")
    global_data["email"] = request.GET.get("email", "")
    global_data["year"] = request.GET.get("year", "")
    global_data["password"] = request.GET.get("password", "")
    global_data["gender"] = request.GET.get("gender", "")
    global_data["final"] = request.GET.get("final", "")
    
    # Debugging: Print received data
    print(f"Received data -> Name: {global_data['name']}, Email: {global_data['email']}, Year: {global_data['year']}, Gender: {global_data['gender']}, Final: {global_data['final']}")
    
    # Respond to the store action (for example, confirming the data is stored)
    return HttpResponse("Data stored successfully.")

def export(request):
    global global_data  # Declare global to access the variable in this function
    
    # Retrieve the data from the global variable
    name = global_data.get("name", "")
    email = global_data.get("email", "")
    year = global_data.get("year", "")
    password = global_data.get("password", "")
    gender = global_data.get("gender", "")
    final = global_data.get("final", "")
    
    # Debugging: Print the data that will be used for email
    print(f"Export Data -> Name: {name}, Email: {email}, Year: {year}, Gender: {gender}, Final: {final}")
    
    if not email or "@" not in email:
        return HttpResponse("Invalid or missing email address.")
    
    try:
        # Send the email
        send_mail(
            "Confirmation Email",
            f"Hello {name},\n\nYour details:\nYear: {year}\nGender: {gender}\nFinal: {final}",
            "narentesting1234@gmail.com",  # Use your email for sending
            [email],
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
        return HttpResponse("Failed to send email. Check server logs.")


def home(request):
    return render(request, 'index.html')

# def store(request):
#     # Retrieving data from GET request
#     name = request.GET.get("name", "")
#     email = request.GET.get("email", "")
#     year = request.GET.get("year", "")
#     password = request.GET.get("password", "")
#     gender = request.GET.get("gender", "")
#     final = request.GET.get("final", "")
    
#     # Debug print statements
#     print(name, email, year, password, gender, final)
    
#     # Combining data into a single context dictionary
#     context = {
#         'name': name,
#         'email': email,
#         'year': year,
#         'password': password,
#         'gender': gender,
#         'final': final
#     }
    
#     # Passing the context dictionary to render
#     return render(request, 'base.html', context)


# def export(request):
#     name = request.GET.get("name", "")
#     email = request.GET.get("email", "")
#     year = request.GET.get("year", "")
#     password = request.GET.get("password", "")
#     gender = request.GET.get("gender", "")
#     final = request.GET.get("final", "")
    
    
    
#     # Debug print statements
#     print(name, email, year, password, gender, final)
    
    
#     send_mail(
#     "Subject here",
#     "Here is the message.",
#     "narentesting1234@gmail.com",
#     ["snarenkumar30@gmail.com"],
#     fail_silently=False,
# )
#     return HttpResponse("done")
# @csrf_exempt
# def export(request):
#     if request.method == "POST":
#         try:
#             # Parse JSON data from request
#             data = json.loads(request.body.decode('utf-8'))
            
#             # Extract values from the received data
#             name = data.get("name", "")
#             email = data.get("email", "")
#             year = data.get("year", "")
#             password = data.get("password", "")
#             gender = data.get("gender", "")
#             final = data.get("final", "")
            
#             # Debug print statements to verify data
#             print(f"Received Data -> Name: {name}, Email: {email}, Year: {year}, Password: {password}, Gender: {gender}, Final: {final}")
            
#             # Validate email (simple check for '@')
#             if not email or "@" not in email:
#                 return JsonResponse({"message": "Invalid or missing email address."}, status=400)
            
#             # Send email (as an example)
#             send_mail(
#                 "Confirmation Email",
#                 f"Hello {name},\n\nYour details:\nYear: {year}\nGender: {gender}\nFinal: {final}",
#                 "narentesting1234@gmail.com",
#                 [email],
#                 fail_silently=False,
#             )
            
#             return JsonResponse({"message": "Email sent successfully."}, status=200)

#         except Exception as e:
#             print(f"Error: {e}")
#             return JsonResponse({"message": "Error processing data."}, status=500)

#     return JsonResponse({"message": "Invalid request method."}, status=405)