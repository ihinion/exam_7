from django import forms
from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['poll']


class AnswerForm(forms.ModelForm):
    def __init__(self, poll_pk, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.poll = Poll.objects.get(pk=poll_pk)

    class Meta:
        model = Answer
        fields = ['choice']

    def clean(self):
        cleaned_data = super(AnswerForm, self).clean()
        choice = Choice.objects.get(text=cleaned_data.get('choice'))
        if choice in self.poll.choice_set.all():
            return cleaned_data
        else:
            raise forms.ValidationError('Select a valid choice. That choice is not one of the available choices.')
