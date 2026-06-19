from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(receipe_name=receipe_name ,receipe_description=receipe_description, receipe_image=receipe_image)

        Queryset = Receipe.objects.all()


            

        return render(request,'receipes.html',{'receipes':Queryset})
    
    
    Queryset1 = Receipe.objects.all()
    return render(request,'receipes.html',{'receipes':Queryset1})


def delete_receipe(request,id):
    obj = Receipe.objects.filter(id=id).delete()
    return redirect('/receips/')

def update_receipe(request,id):
    obj = Receipe.objects.get(id=id)


    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        obj.receipe_name = receipe_name 
        obj.receipe_description = receipe_description
        if receipe_image:
            obj.receipe_image=receipe_image

        obj.save()
        return redirect('/receips/')

    

    return render(request,'update_receipes.html',{'receipes':obj})