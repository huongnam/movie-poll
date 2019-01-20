from django.shortcuts import render, redirect

def welcome(request):
    if request.user.is_authenticated:
        return redirect('movieholic_home')
    else:
        return render(request, 'pythonweb/welcome.html')