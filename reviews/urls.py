# reviews/urls.py

from django.urls import path
from .views import main_views, ticket_views, review_views, follow_views


urlpatterns = [
    # Main
    path('', main_views.flux, name='flux'),
    path('posts/', main_views.user_posts, name='user-posts'),

    # Following
    path('following/', follow_views.following, name='following'),
    path('unfollow/<int:following_id>', follow_views.unfollow, name='unfollow'),

    # Ticket
    path('ticket/create/', ticket_views.ticket_create, name='ticket-create'),
    path('ticket/<int:ticket_id>/update/', ticket_views.ticket_update, name='ticket-update'),
    path('ticket/<int:ticket_id>/delete/', ticket_views.ticket_delete, name='ticket-delete'),

    # Reviews
    path('reviews/create/', review_views.ticket_and_review_create, name='ticket-and-review-create'),
    path('ticket/<int:ticket_id>/reviews/create/', review_views.review_create, name='review-create'),
    path('reviews/<int:review_id>/update/', review_views.review_update, name='review-update'),
    path('reviews/<int:review_id>/delete/', review_views.review_delete, name='review-delete'),
]
