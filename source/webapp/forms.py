from django import forms
from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['poll']