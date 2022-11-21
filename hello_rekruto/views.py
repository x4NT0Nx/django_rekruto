from django.http import HttpResponse
from django.shortcuts import render
  
def index(request):
    name = request.GET.get("name")
    message = request.GET.get("message")
    data = {"text1": name, "text2": message}
    return render(request, "pattern.html", context = data)
    
