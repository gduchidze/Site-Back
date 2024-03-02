from django.shortcuts import render

posts = [
    {
        'author': 'Giorgi Duchidze',
        'title': 'Nike x Travis scott 1',
        'content': 'shoes',
        'date_posted': 'March 2, 2024',
    },
{
        'author': 'Tato Dznelashvili',
        'title': 'Adidas Samba',
        'content': 'shoes',
        'date_posted': 'March 1, 2024',
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

