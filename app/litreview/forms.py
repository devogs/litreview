# app/litreview/forms.py
from django import forms
from .models import Ticket
from .models import Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4}),
        }