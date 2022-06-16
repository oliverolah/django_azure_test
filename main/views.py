from django.shortcuts import render
from django.http import HttpResponse


def returnHomePage(request):
  return render(request, "main/home.html")
