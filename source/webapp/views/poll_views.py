from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm
from webapp.models import Poll


class PollView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_at')
        return queryset


class PollCreateView(CreateView):
    template_name = 'poll/poll_create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    template_name = 'poll/poll_update.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    success_url = reverse_lazy('index_view')