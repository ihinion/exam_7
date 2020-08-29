from django.contrib import admin
from webapp.models import Poll, Choice, Answer

# superuser
# login: admin
# password: admin
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Answer)