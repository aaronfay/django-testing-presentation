from django.shortcuts import render

from hackers.forms import SignupForm
from hackers.models import Participant
from hackers import registrar


def signup(request):
    if request.method == 'POST':
        # - take the email from the request
        # - save the user in the database
        # - if they're not staff, email them a thank you
        form = SignupForm(request.POST)
        if form.is_valid():
            registrar.add_participant(form.cleaned_data['email'])

    form = SignupForm()
    return render(request, 'hackers/signup.html', {'form': form})