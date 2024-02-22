from django.shortcuts import render
from .models import Oddeleni
# Create your views here.


def index(request):
    return render(request, "oddeleni/index.html", {
        "oddeleni": Pokoje.objects.all()
    })