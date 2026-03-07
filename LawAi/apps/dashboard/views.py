from django.shortcuts import render,redirect


def lawyer_dashboard(request):

    if 'user_id' not in request.session:
        return redirect("/api/signing/login/")

    return render(request,"dashboard/lawyer_dashboard.html",{"role":"lawyer"})