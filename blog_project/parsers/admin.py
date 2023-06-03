from django.contrib import admin
from parsers.models import Parser

# Register your models here.

@admin.register(Parser)
class ParserAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'company', 'years_of_experience', 'location', 'description', 'required_skills', 'type', 'job_time_posted')
    list_filter = ('name', 'title', 'company', 'years_of_experience', 'location',  'type', 'job_time_posted')

