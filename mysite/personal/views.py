from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'personal/home.html')
'''
def contact(request):
	return render(request,'personal/basic.html',{'content':['Email:','<b>ben.suutari@gmail.com</b>','Github:','github.com/moejamin','Reddit:','reddit.com']})

# Create your views here.
'''