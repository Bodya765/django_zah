from django.shortcuts import render


def index(request):
    data = {
        'title': 'Головна',
        'values': ['Some','Hello','123'],
        'obj':{
            'car':'BMW',
            'age': 18,
            'hobby':"Football"
        }
    }
    return render(request,'home/index.html', data)

def about(request):
    return render(request, 'home/about.html')


