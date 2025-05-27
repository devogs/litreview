# accounts/views.py 
from django.shortcuts import render, redirect
from django.contrib.auth import login # Import login for automatic login after signup
from .forms import SignUpForm # Make sure this imports your corrected SignUpForm
from django.contrib.auth import get_user_model # If you needed to get the user model here for other reasons

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) # Create instance of your form
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately after signup
            return redirect('flux') # Redirect to your desired page after signup
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})