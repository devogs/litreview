# app/litreview/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('flux/', views.flux, name='flux'),
    path('add-ticket/', views.add_ticket, name='add_ticket'),
    path('edit-ticket/<int:ticket_id>/', views.add_ticket, name='edit_ticket'),
    path('delete-ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    path('add-review/', views.add_review, name='add_review_no_ticket'),
    path('add-review/<int:ticket_id>/', views.add_review, name='add_review'),
    path('edit-review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
]