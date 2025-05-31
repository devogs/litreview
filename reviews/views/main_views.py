# reviews/views/main_views.py
from itertools import chain

from .utils_views import get_users_viewable_tickets, get_users_viewable_reviews

from django.db.models import Value, CharField
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from .. import forms, models


@login_required
def flux(request):
    """
    Main page. Show a flux of tickets and reviews depending on the user's follows
    that use helper functions and annotate content type.
    """
    tickets = get_users_viewable_tickets(request.user)
    reviews = get_users_viewable_reviews(request.user)

    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    context = {
        'posts': posts,
        'flux_page': True,
        'navbar': 'flux',
    }
    return render(request, 'reviews/flux.html', context)

@login_required
def user_posts(request):
    """
    Show the tickets and reviews created by the user.
    They can be modified or deleted here.
    """
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    post_page = True
    context = {
        'tickets_and_reviews': tickets_and_reviews,
        'post_page': post_page,
        'navbar': 'posts',
    }
    return render(request, 'reviews/user_posts.html',
                  context)
