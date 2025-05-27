# accounts/forms.py (corrected)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model # Import get_user_model

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model() 
        fields = UserCreationForm.Meta.fields
