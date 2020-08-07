from django.shortcuts import render
from django.http import HttpResponse
import operator

def index(request):
	return render(request,"index.html",)

