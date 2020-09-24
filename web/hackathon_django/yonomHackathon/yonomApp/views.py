from django.shortcuts import render, redirect
from .models import login, game_data, Bangkoker
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def test2(request):
    return render(request, 'test2.html')
    
def web_home(request):

    return render(request, 'web_home.html')


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




def data_insert(request):

    
    user_names = request.user.username


    data1 = request.FILES['image1']
    data2 = request.FILES['image2']
    data3 = request.FILES['image3']
    data4 = request.FILES['image4']
    data5 = request.FILES['image5']
    data6 = request.FILES['image6']
    data7 = request.FILES['image7']
    data8 = request.FILES['image8']
    data9 = request.FILES['image9']
    
    
    game_datas = game_data(user_name = user_names, bingo1=data1 , bingo2=data2, bingo3=data3,bingo4=data4 ,bingo5=data5, bingo6=data6, bingo7=data7, bingo8=data8, bingo9=data9)
    game_datas.save()

    # if game_data.objects.get(user_name=name):
    #     data_delete = game_data.objects.get(user_name=name)
    #     data_delete.delete()

    #     data_input = game_data(user_name = name, bingo1 = all_data[0], bingo2 = all_data[1], bingo3 = all_data[2], bingo4 = all_data[3], bingo5 = all_data[4], bingo6 = all_data[5], bingo7 = all_data[6], bingo8 = all_data[7], bingo9 = all_data[8])
    #     data_input.save()
        
    #     user_data = game_data.objects.get(user_name=name)
    
    context = { 'game_data' : game_datas}

    return render(request, 'game_home.html', context)




def web_home(request):

    return render(request, 'web_home.html')




ERROR_MSG = {
    # 'ID_EXIST': "이미 사용 중인 닉네임입니다.",
    'ID_NOT_EXIST': "정보가 존재하지 않습니다. 입력한 정보로 가입하시겠습니까?",
    'ID_PW_MISSING': "닉네임과 비밀번호를 확인하세요.",
    'PW_CHECK' : "비밀번호가 일치하지 않습니다."
}



def game_login(request):
    context = {
        'error': {
            'state': False,
            'condition':'',
            'msg': '',
        },
        'user_id':'',
        'user_pw':'',
    }

    
    if request.method == "POST":

        if request.POST['flag']=='signup':
            user_id = request.POST['user_id']
            user_pw = request.POST['user_pw']

            user = User.objects.create_user(
                username=user_id,
                password=user_pw,
            )
            Bangkoker.objects.create(
                user=user
            )

            auth.login(request, user)

            return render(request, 'game_home.html')
            


        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        context['user_id'] = user_id
        context['user_pw'] = user_pw

        user = User.objects.filter(username=user_id)

        if user_id and user_pw:      
            if len(user) > 0:
                
                user = auth.authenticate(
                    username=user_id,
                    password=user_pw
                )
                
                if user != None:
                    auth.login(request, user)
                    
                    context = {'user': user}
                    return render(request, 'game_home.html', context)  
                
                else:
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
                    context['error']['state'] = True          

            else:
                context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']
                context['error']['state'] = True   
                context['error']['condition'] = 'ID_NOT_EXIST'
                
                # > 정보가 존재하지 않습니다. 입력한 정보로 가입하시겠습니까?
                    ## >> Y : create_user
                    ## >> N : redirect login page

        else: 
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']
            context['error']['state'] = True    

         
    return render(request, 'game_login.html', context)



def logout(request):
    auth.logout(request)
    return redirect('web_home')