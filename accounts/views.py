# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


def signup(request):
    """
    Handles user registration.

    If the request method is POST, it attempts to validate and save
    the user's registration form. If successful, the user is
    automatically logged in and redirected to the 'flux' page.
    If the form is invalid, it re-renders the signup page with errors.

    If the request method is GET, it displays an empty registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the signup page with the form, or
                      redirects to 'flux' upon successful registration.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flux')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
