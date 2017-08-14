from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf

# Create your views here.


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '') # Получить из пост запроса юзернейм
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password) # Отправляю логин и пароль в auth
        if user is not None:
            auth.login(request, user) # Авторизация найденного пользователя
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request) # Делогон пользователя
    return redirect('/')
