# reviews/templatetags/review_extras.py
from django import template
from reviews.models import Review # Ensure Review model is imported here
from django.db.models import Q # Add if not already there, for potential future complex queries

register = template.Library()


@register.filter
def model_type(value):
    """
    Return the type of the model.
    """
    return type(value).__name__


@register.filter
def format_date(time_created):
    """
    Return a formatted date.
    """
    return f'{time_created.strftime("%H:%M, %d %B %Y")}'


@register.filter
def show_rating(rating):
    """
    Return a string composed of stars depending on the rating.
    """
    stars = ''
    for i in range(rating):
        stars += '★'
    for i in range(5 - rating):
        stars += '☆'
    return stars


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    """
     Return a name to display depending on the current user.
    """
    if user == context['user']:
        return 'Vous'
    return user.username


@register.simple_tag(takes_context=True)
def get_ticket_poster_display(context, user):
    """
    Return the ticket poster to display depending on the current user.
    """
    if user == context['user']:
        return 'Vous avez demandé une critique.'
    return f'{user.username} a demandé une critique.'


@register.simple_tag(takes_context=True)
def get_review_poster_display(context, user):
    """
     Return the review poster to display depending on the current user.
    """
    if user == context['user']:
        return 'Vous avez publié une critique.'
    return f'{user.username} a publié une critique.'


# MODIFIED TAG for Option B (any review exists for ticket)
@register.simple_tag
def has_any_review_for_ticket(ticket):
    """
    Returns True if ANY review exists for the given ticket, False otherwise.
    """
    return Review.objects.filter(ticket=ticket).exists()


# NEW TAG for current user's review
@register.simple_tag(takes_context=True)
def get_user_review_for_ticket(context, ticket):
    """
    Returns the Review object if the current user has already reviewed the given ticket,
    otherwise returns None.
    """
    # Using .first() will return the object or None if it doesn't exist
    return Review.objects.filter(ticket=ticket, user=context['user']).first()