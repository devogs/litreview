# reviews/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.flux, name='flux'),
    path('posts/', views.user_posts, name='user-posts'),
    path('following/', views.following, name='following'),
    path('unfollow/<int:following_id>', views.unfollow, name='unfollow'),
    path('ticket/create/', views.ticket_create, name='ticket-create'),
    path('ticket/<int:ticket_id>/update/', views.ticket_update, name='ticket-update'),
    path('ticket/<int:ticket_id>/delete/', views.ticket_delete, name='ticket-delete'),
    path('reviews/create/', views.ticket_and_review_create, name='ticket-and-review-create'),
    path('ticket/<int:ticket_id>/reviews/create/', views.review_create, name='review-create'),
    path('reviews/<int:review_id>/update/', views.review_update, name='review-update'),
    path('reviews/<int:review_id>/delete/', views.review_delete, name='review-delete'),
]