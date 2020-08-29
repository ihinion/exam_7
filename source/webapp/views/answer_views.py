from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from webapp.forms import AnswerForm
from webapp.models import Answer, Poll, Choice


class AnswerCreateView(CreateView):
    template_name = 'answer/answer_create.html'
    model = Answer
    form_class = AnswerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        poll = self.get_poll()
        context['form'].fields['choice'].queryset = Choice.objects.filter(poll=poll)
        context['poll'] = poll
        return context

    def get_form_kwargs(self):
        kwargs = super(AnswerCreateView, self).get_form_kwargs()
        kwargs['poll_pk'] = self.kwargs.get('pk')
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_poll()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.poll = self.poll
        answer.save()
        return redirect('poll_view', pk=self.poll.pk)

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})