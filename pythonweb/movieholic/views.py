from django.shortcuts import render
from moviepoll.models import Question
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
@login_required
def home(request):
    return render(request, "movieholic/home.html",
                    {'all_question': Question.objects.all()})

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "movieholic/signup_form.html"
    success_url = reverse_lazy('movieholic_home')