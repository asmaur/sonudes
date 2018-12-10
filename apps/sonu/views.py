from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "sonu/coming.html")


def error_404_view(request, exception):
    return render(request,'sonu/error.html', {}, status=404)

def error_403_view(request, exception):
    return render(request,'sonu/error.html', {}, status=403)