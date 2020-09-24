from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Bangkoker
from django.contrib import auth

# Create your views here.
def web_home(request):

    return render(request, 'web_home.html')



ERROR_MSG = {
    # 'ID_EXIST': "이미 사용 중인 닉네임입니다.",
    'ID_NOT_EXIST': "정보가 존재하지 않습니다. 입력한 정보로 가입하시겠습니까?",
    'ID_PW_MISSING': "닉네임과 비밀번호를 확인하세요.",
    'PW_CHECK' : "비밀번호가 일치하지 않습니다."
}



def login(request):
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
                    return render(request, 'game.html', context)  
                
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

        
    print('♥♥♥♥♥♥♥♥♥♥♥♥', context)    
    return render(request, 'login.html', context)


def signup(request):
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
    return render(request, 'game.html')


    def logout(request):
        auth.logout(request)
        return redirect('home')