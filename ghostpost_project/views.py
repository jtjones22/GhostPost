from django.shortcuts import (
    render,
    reverse,
    HttpResponseRedirect
    )

from .models import PostItem
from .forms import AddPost


def is_valid_query(parameter):
    return True if parameter else False


def index(request):
    qs = PostItem.objects.all()
    qs = qs.order_by('-submission_time')
    # categories = Category.objects.all()
    votes = request.GET.get('votes')
    category = request.GET.get('category')
    if is_valid_query(category) and category != 'Choose Category...':
        if category == 'roasts':
            qs = qs.filter(category_choice='roast')
        elif category == 'boasts':
            qs = qs.filter(category_choice='boast')
        else:
            pass
    if is_valid_query(votes):
        qs = sorted(qs, key=lambda post: post.vote_score, reverse=True)
    html = 'index.html'
    context = {'posts': qs, 'category': category, 'votes': votes}
    return render(request, html, context)


def post(request, post_id):
    item = PostItem.objects.get(id=post_id)
    html = 'post.html'
    context = {'post': item}
    return render(request, html, context)


def upvote(request, post_id):
    post = PostItem.objects.get(id=post_id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('post', kwargs={'post_id': post_id}))


def downvote(request, post_id):
    post = PostItem.objects.get(id=post_id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('post', kwargs={'post_id': post_id}))


def add_post(request):
    html = 'addpost.html'
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PostItem.objects.create(
                category_choice=data['category_choice'],
                text=data['text']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddPost()

    context = {'form': form}
    return render(request, html, context)



"""
Originally had these linked on the index page to go to another page to sort the PostItems
Then decided to try to get the drop down category working
"""
# def roast_posts(request):
#     items = PostItem.objects.filter()
#     items = items.order_by('-submission_time')
#     html = 'roast_posts.html'
#     context = {'posts': items}
#     return render(request, html, context)


# def boast_posts(request):
#     items = PostItem.objects.filter()
#     items = items.order_by('-submission_time')
#     html = 'boast_posts.html'
#     context = {'posts': items}
#     return render(request, html, context)