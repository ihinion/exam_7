from django.db import models


class Poll(models.Model):
    text = models.CharField(max_length=200, verbose_name='Poll text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.TextField(max_length=1000, verbose_name='Choice text')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE,
                             verbose_name='Poll FK')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.text