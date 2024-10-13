from django.shortcuts import render


def platform_view(request):
    return render(request, 'fourth_task/platform.html')


def games_view(request):
    # Изменяем словарь на список
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    return render(request, 'fourth_task/games.html', {'games': games})


def cart_view(request):
    return render(request, 'fourth_task/cart.html')
