# reviews/views/follow_views.py

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from accounts.models import User
from .. import forms, models


@login_required
def following(request):
    """
    Page to manage the users to follow.
    Includes handling for duplicate follows and uses Django messages for all feedback.
    """
    form = forms.UserFollowsForm(user=request.user)

    followed_users = models.UserFollows.objects.filter(user=request.user)
    following_users = models.UserFollows.objects.filter(followed_user=request.user)

    if request.method == 'POST':
        form = forms.UserFollowsForm(request.user, request.POST)
        if form.is_valid():
            followed_user_instance = form.cleaned_data['followed_user']

            if not models.UserFollows.objects.filter(user=request.user, followed_user=followed_user_instance).exists():
                user_follows = form.save(commit=False)
                user_follows.user = request.user
                user_follows.save()
                messages.success(request, f"You are now following {followed_user_instance.username}.")
            else:
                messages.warning(request, f"You are already following {followed_user_instance.username}.")
            
            return redirect('following')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field == '__all__':
                        messages.error(request, error)
                    else:
                        field_label = form.fields[field].label if form.fields[field].label else field.replace('_', ' ').capitalize()
                        messages.error(request, f"{error}")

    context = {
        'form': form,
        'followed_users': followed_users,
        'following_users': following_users,
        'navbar': 'following',
    }
    return render(request, 'reviews/following.html', context=context)


@login_required
def unfollow(request, following_id):
    """
    Allow to unfollow a user.
    """
    user_follows = get_object_or_404(models.UserFollows, id=following_id)
    user_follows.delete()
    return redirect('following')
