from django.http import JsonResponse
from .models import User
from django.shortcuts import render

from django.shortcuts import redirect


def signup(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = User.objects.create(
            name=name,
            email=email,
            password=password,
            role=role
        )
        
        request.session['user_id'] = user.id
        request.session['role'] = user.role

        # Redirect based on role
        if role == "lawyer":
            return redirect("/api/dashboard/lawyer/")
        else:
            return redirect("/api/dashboard/user/")

    return render(request, "signing/signup.html")
    


    
def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email, password=password)
            
            
            request.session['user_id'] = user.id
            request.session['role'] = user.role

            # Redirect based on role
            if user.role == "lawyer":
                return redirect("/api/dashboard/lawyer/")
            else:
                return redirect("/api/dashboard/user/")

        except User.DoesNotExist:
            return render(request, "signing/login.html", {
                "error": "Invalid email or password"
            })

    return render(request, "signing/login.html")



def logout_view(request):
    request.session.flush()   
    return redirect("/api/signing/login/")