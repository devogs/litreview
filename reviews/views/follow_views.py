# reviews/views/follow_views.py

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import User
from .. import forms, models


@login_required
def following(request):
    """
    Page to manage the users to follow.
    """
    form = forms.UserFollowsForm(user=request.user)
    followed_users = models.UserFollows.objects.filter(user=request.user)
    following_users = models.UserFollows.objects.filter(followed_user=request.user)
    if request.method == 'POST':
        form = forms.UserFollowsForm(request.user, request.POST)
        if form.is_valid():
            user_follows = form.save(commit=False)
            user_follows.user = request.user
            user_follows.save()
            return redirect('following')
    context = {
        'form': form,
        'followed_users': followed_users,
        'following_users': following_users,
        'navbar': 'following',
    }
    return render(request, 'reviews/following.html',
                  context=context)


@login_required
def unfollow(request, following_id):
    """
    Allow to unfollow a user.
    """
    user_follows = get_object_or_404(models.UserFollows, id=following_id)
    user_follows.delete()
    return redirect('following')
