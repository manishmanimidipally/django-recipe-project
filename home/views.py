from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):

    peoples=[
        {'name':'Abhijeet Gupta','age':19,"country":'America'},
        {'name':'nilesh','age':18,'country':'india'},
        {'name':'ganesh','age':22,'country':'india'},
        {'name':'umesh','age':24,'country':'germany'},
        {'name':'Rishi','age':26,'country':'india'},
    ]
    return render(request,'home/index.html',context={'peoples':peoples})

def success_page(request):
    return HttpResponse("<h1> hey manish how are you </h1>")