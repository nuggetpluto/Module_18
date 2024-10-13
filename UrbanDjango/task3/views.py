from django.shortcuts import render


# Главная страница
def platform_view(request):
    return render(request, 'third_task/platform.html')


# Страница "Магазин"
def games_view(request):
    # Словарь с играми
    games = {
        'Atomic Heart': 'Купить',
        'Cyberpunk 2077': 'Купить',
        'PayDay 2': 'Купить'
    }
    return render(request, 'third_task/games.html', {'games': games})


# Страница "Корзина"
def cart_view(request):
    return render(request, 'third_task/cart.html')
