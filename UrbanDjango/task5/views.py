from django.shortcuts import render
from .forms import UserRegisterForm

# Псевдосписок существующих пользователей
users = ['vasya', 'petya', 'masha']


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # Проверки
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['success'] = f"Приветствуем, {username}!"
            users.append(username)

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    form = UserRegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        repeat_password = form.cleaned_data.get('repeat_password')
        age = form.cleaned_data.get('age')

        # Проверки
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['success'] = f"Приветствуем, {username}!"
            users.append(username)

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)
