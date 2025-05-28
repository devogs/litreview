# reviews/forms.py
from django import forms
from django.db.models import Q
from django.shortcuts import get_object_or_404

from accounts.models import User
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        choices = (
            ('0', 0), ('1', 1), ('2', 2),
            ('3', 3), ('4', 4), ('5', 5),
        )
        widgets = {'rating': forms.RadioSelect(choices=choices)}


class UserFollowsForm(forms.ModelForm):
    followed_user = forms.CharField(
        max_length=150,
        label='Nom d\'utilisateur à suivre',
        widget=forms.TextInput(attrs={'list': 'followed_users'})
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        self.choices = User.objects.all().exclude(
            Q(followed_by__in=self.user.following.all())
            | Q(id=self.user.id)
        ).values('username')

    def clean_followed_user(self):
        username = self.cleaned_data['followed_user']
        try:
            user_to_follow = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Cet utilisateur n'existe pas.")

        if user_to_follow == self.user:
            raise forms.ValidationError("Vous ne pouvez pas vous suivre vous-même.")

        if models.UserFollows.objects.filter(user=self.user, followed_user=user_to_follow).exists():
            raise forms.ValidationError("Vous suivez déjà cet utilisateur.")

        return user_to_follow

    class Meta:
        model = models.UserFollows
        fields = ['followed_user']
