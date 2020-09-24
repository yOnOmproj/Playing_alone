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
    # if request.POST['name']:
    #     login_name = request.POST['name']


    #     all_login_data = login.objects.all()

    #     if login_name in all_login_data.name:
    #         user_data = game_data.objects.get(user_name=login_name) 

    #     else:
    #         create_user = login(name=login_name)
    #         create_user.save()

    #         create_user_data = game_data(user_name=login_name)
    #         create_user_data.save()

    #         user_data = game_data.objects.get(user_name = login_name)


    return render(request, 'game_home.html')

def game_result(request):

    user_data = login.objects.get(name = "성빈")

    context = { 'user_data' : user_data}

    return  render(request, 'game_result.html', context)

def assert_login(request):
    name = request.POST['name']
    all_data = login.objects.all()

    print(name)

    all_data_name = []
    for data in all_data:
        all_data_name.append(data.name)

    if name in all_data_name:
        print("유저 아이디 있음")
        user_data = game_data.objects.get(user_name = name)
    else:
        print("유저 아이디 없다")
        create_name = login(name=name)
        create_name.save()

        create_data = game_data(user_name=name)
        create_data.save()

        user_data = game_data.objects.get(user_name=name)

    
    

    context = { 'user_data' : user_data}
    return render(request, 'game_home.html', context)

def data_insert(request):
    name = request.POST['onloggin'] 
    print(name)
    data = request.FILES['image']
    if game_data.objects.get(user_name=name):
        data_delete = game_data.objects.get(user_name=name)
        data_delete.delete()

        data_input = game_data(user_name = name, bingo1 = data)
        data_input.save()
    
    user_data = game_data.objects.get(user_name=name)
    
    context = { 'user_data' : user_data}

    return render(request, 'game_home.html', context)