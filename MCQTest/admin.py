from django.contrib import admin
from . import models

admin.site.register(models.Question)
admin.site.register(models.Choice)
admin.site.register(models.Answers)
admin.site.register(models.Category)
