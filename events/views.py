from django.shortcuts import render
from .models import Event, Category
from datetime import date


def home(request):
    today = date.today()

    events = Event.objects.filter(date__gte=today).order_by('date')
    categories = Category.objects.all()

    selected_date = request.GET.get('date')
    selected_category = request.GET.get('category')git
    today_filter = request.GET.get('today')

    # кнопка Сегодня
    if today_filter:
        events = events.filter(date=today)

    # фильтр по дате вручную
    elif selected_date:
        events = events.filter(date=selected_date)

    # категория
    if selected_category:
        events = events.filter(category_id=selected_category)

    selected_category_name = None

    if selected_category:
        selected_category_name = Category.objects.get(id=selected_category).name



    # реальные события на сегодня
    today_count = Event.objects.filter(date=today).count()

    context = {
        'events': events,
        'categories': categories,
        'today_count': today_count,
        'today': today,
        'selected_date': selected_date,
        'selected_category_name': selected_category_name,
    }

    return render(request, 'events/home.html', context)
