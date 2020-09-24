from django.shortcuts import render
from .models import login, game_data

# Create your views here.
def test2(request):
    return render(request, 'test2.html')
    
def web_home(request):

    return render(request, 'web_home.html')


def game_login(request):

    return render(request, 'game_login.html')


def game_home(request):
    ## login data가 있는 경우
    if request.POST['name']:
        login_name = request.POST['name']


        all_login_data = login.objects.all()

        if login_name in all_login_data.name:
            user_data = login.objects.get(user_name=login_name) 

        else:
            create_user = login(name=login_name)
            create_user.save()

            create_user_data = game_data(user_name=login_name)
            create_user.data.save()
    else:
        pass
    return render(request, 'game_home.html')
def game_result(request):


    return  render(request, 'game_result.html')