from django.shortcuts import render
from django.http import HttpResponse
from django.utils import html


def index (request):
	return render(request,'main/index.html')

def about (request):
	return HttpResponse("нихуя")