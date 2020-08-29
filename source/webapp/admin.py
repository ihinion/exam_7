from django.contrib import admin
from webapp.models import Poll, Choice

# superuser
# login: admin
# password: admin
admin.site.register(Poll)
admin.site.register(Choice)