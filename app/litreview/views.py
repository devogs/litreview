# app/litreview/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm
from .models import Review
from .forms import ReviewForm

def home(request):
    # Serve login form (Page 1) for unauthenticated users
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('flux')  # Redirect to /flux/ after login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def signup(request):
    # Serve signup form (Page 2)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to / (login page) after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def flux(request):
    # Placeholder for flux page (to be implemented in Phase 3)
    return render(request, 'flux.html')

@login_required
def add_ticket(request, ticket_id=None):
    if ticket_id:
        ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    else:
        ticket = None

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            updated_ticket = form.save(commit=False)
            if not ticket:  # New ticket
                updated_ticket.user = request.user
            updated_ticket.save()
            return redirect('flux')
    else:
        form = TicketForm(instance=ticket) if ticket else TicketForm()
    return render(request, 'add_ticket.html', {'form': form})

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        ticket.delete()
        return redirect('flux')
    return render(request, 'confirm_delete_ticket.html', {'ticket': ticket})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a Ticket for the book
            ticket = Ticket.objects.create(
                user=request.user,
                title=form.cleaned_data['book_title'],
                description="",  # Optional description for the ticket
                image=request.FILES.get('image', None),  # Handle image upload
            )
            # Create the Review
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.rating = form.cleaned_data['rating']
            review.save()
            messages.success(request, "Critique ajoutée avec succès!")
            return redirect('flux')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('flux')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'add_review.html', {'form': form, 'ticket': review.ticket})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('flux')
    return render(request, 'confirm_delete_review.html', {'review': review})