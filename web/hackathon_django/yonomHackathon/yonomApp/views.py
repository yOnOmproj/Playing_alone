from django.shortcuts import render

# Create your views here.
def web_home(request):

    return render(request, 'web_home.html')