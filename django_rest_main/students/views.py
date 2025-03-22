from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students = [
        {"id": 1,"name": "Sneha","class": "Django"}
    ]
    return HttpResponse(students)

def snehagod(request):
    students = [
        {"id": 2,"name": "PRMIUM","class": "COMPUTER"}
    ]
    return HttpResponse(students)
