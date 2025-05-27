# reviews/admin.py
from django.contrib import admin
from .models import Ticket, Review, UserFollows # Assuming these models are in reviews/models.py

admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(UserFollows)