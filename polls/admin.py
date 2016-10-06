from django.contrib import admin
from .models import Question, Choice, Human

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Human)
