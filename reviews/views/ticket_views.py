# reviews/views/ticket_views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .. import forms, models


@login_required
def ticket_create(request):
    """
    Page with a form to create a ticket.
    """
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    context = {
        'form': form,
        'navbar': 'flux',
    }
    return render(request, 'reviews/ticket_create.html',
                  context=context)


@login_required
def ticket_update(request, ticket_id):
    """
    Page with a form to modify an existing ticket.
    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('user-posts')
    context = {
        'form': form,
        'navbar': 'posts',
    }
    return render(request, 'reviews/ticket_update.html',
                  context=context)


@login_required
def ticket_delete(request, ticket_id):
    """
    Page to delete a ticket.
    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    ticket.delete()
    return redirect('user-posts')
