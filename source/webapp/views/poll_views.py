from django.shortcuts import render
from django.views.generic import DetailView, ListView
from webapp.models import Poll


class PollView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    paginate_by = 2
