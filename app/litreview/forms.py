# app/litreview/forms.py
from django import forms
from .models import Review, Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image (facultatif)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class ReviewForm(forms.ModelForm):
    book_title = forms.CharField(
        label="Titre du livre",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(0, 6)],
        widget=forms.RadioSelect,
        label="Note",
        required=False,  # Allow the field to be optional
        initial=0,  # Default to 0 if not selected
    )

    class Meta:
        model = Review
        fields = ['headline', 'body', 'rating']
        labels = {
            'headline': 'Titre de la critique',
            'body': 'Description',
        }
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].label = "Note"