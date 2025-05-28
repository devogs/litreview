# reviews/views/review_views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .. import forms, models


@login_required
def ticket_and_review_create(request):
    """
    Page with a form to create both a ticket and its corresponding review.
    """
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()

    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
        'navbar': 'flux',
    }
    return render(request, 'reviews/ticket_and_review_create.html',
                  context=context)


@login_required
def review_create(request, ticket_id):
    """
    Page with a form to create a review.
    """
    ticket = models.Ticket.objects.get(id=ticket_id)
    form = forms.ReviewForm()

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')
    context = {
        'ticket': ticket,
        'form': form,
        'navbar': 'flux',
    }
    return render(request, 'reviews/review_create.html',
                  context=context)


@login_required
def review_update(request, review_id):
    """
    Page with a form to modify an existing review.
    """
    review = get_object_or_404(models.Review, id=review_id)
    form = forms.ReviewForm(instance=review)

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('user-posts')
    context = {
        'form': form,
        'review': review,
        'navbar': 'posts',
    }
    return render(request, 'reviews/review_update.html',
                  context=context)


@login_required
def review_delete(request, review_id):
    """
    Page to delete a review.
    """
    review = get_object_or_404(models.Review, id=review_id)
    review.delete()
    return redirect('user-posts')
