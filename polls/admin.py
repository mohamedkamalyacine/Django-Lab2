from django.contrib import admin
from .models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

# admin.site.site_header = "Pollster Admin"
# admin.site.site_title = "Pollster Admin Area"
# admin.site.index_title = "Welcome to Pollestre Admin Area"

# class ChoiceInLine(admin.TabularInline):
#     model = Selection
#     extra = 3

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [(None, )]