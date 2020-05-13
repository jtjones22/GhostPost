from django.shortcuts import (
    render,
    reverse,
    HttpResponseRedirect
    )

# from .models import PostItem


def index(request):
    items = PostItem.objects.all()
    return render(
        request,
        'index.html',
        {
            'posts': items
        }
        
    )