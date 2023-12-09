from django.shortcuts import render

def original(request):
    return render(request, "core/original.html")