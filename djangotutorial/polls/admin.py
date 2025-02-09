from django.contrib import admin
# ".models" first accesses the current package we're in with . (polls) and then finds model.py
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
