from django.shortcuts import render
from django.views.generic import DetailView
from webapp.models import Poll


class PollView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll
