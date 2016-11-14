from django.shortcuts import render

from hackers.forms import SignupForm
from hackers.models import Participant


def signup(request):
    if request.method == 'POST':
        # - take the email from the request
        # - save the user in the database
        # - if they're not staff, email them a thank you
        form = SignupForm(request.POST)
        if form.is_valid():
            participant = Participant(email=form.cleaned_data['email'])
            participant.save()

    form = SignupForm()
    return render(request, 'hackers/signup.html', {'form': form})