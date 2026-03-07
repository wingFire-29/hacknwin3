from django.shortcuts import render

def lawyer_dashboard(request):
    return render(request,"dashboard/lawyer_dashboard.html")


def user_dashboard(request):
    return render(request,"dashboard/user_dashboard.html")