from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import News, Category
from .forms import NewsForm


def news_list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    query = request.GET.get('query')
    if category_id:
        news = News.objects.filter(category_id=category_id)
    else:
        news = News.objects.all()
    if query:
        news = news.filter(title__icontains=query)
    return render(request, 'news/news_home.html', {'news': news, 'categories': categories})


def news_home(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        news = News.objects.filter(category_id=category_id)
    else:
        news = News.objects.all()

    return render(request, 'news/news_home.html', {'news': news, 'categories': categories})


def edit_announcement(request, id):
    announcement = get_object_or_404(News, pk=id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=announcement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Оголошення успішно оновлено.')
            return redirect('news_home')
    else:
        form = NewsForm(instance=announcement)
    return render(request, 'news/edit_announcement.html', {'form': form})


def delete_announcement(request, id):
    announcement = get_object_or_404(News, pk=id)
    announcement.delete()
    messages.success(request, 'Оголошення успішно видалено.')
    return redirect('news_home')


def create_announcement(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Оголошення успішно створено.')
            return redirect('news_home')
    else:
        form = NewsForm()
    return render(request, 'news/create.html', {'form': form})
