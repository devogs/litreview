# reviews/views/utils_views.py
from django.db.models import Q, Value, CharField
from reviews import models


def get_users_viewable_tickets(user):
    """
    Returns a queryset of tickets viewable by the given user.
    This includes tickets from followed users and tickets created by the user.
    """
    user_follows = models.UserFollows.objects.filter(user=user).values('followed_user')
    tickets = models.Ticket.objects.filter(
        Q(user__in=user_follows) | Q(user=user)
    )
    return tickets

def get_users_viewable_reviews(user):
    """
    Returns a queryset of reviews viewable by the given user.
    This includes reviews from followed users, reviews created by the user,
    and reviews made in response to the user's tickets.
    """
    user_follows = models.UserFollows.objects.filter(user=user).values('followed_user')
    reviews = models.Review.objects.filter(
        Q(user__in=user_follows) | Q(user=user) | Q(ticket__user=user)
    )
    return reviews