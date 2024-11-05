from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Talaba

def index(request):
    return render(request, "malumot.html")

def salom(request):
        return render(request, "Mualif.html")

def talabalar(request):
    param = request.GET.get("search")
    students = Talaba.objects.all()
    if param:
        students = students.filter(ism__contains=param)
    context = {
        "students":Talaba.objects.all()
    }
    return render(request, "talabalar.html", context)

def delete_student(request, id):
    talaba = Talaba.objects.get(id=id)
    talaba.delete()
    return redirect("/talabalar/")