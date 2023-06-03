
from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Parser(models.Model):
    name = models.ForeignKey(Job, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    years_of_experience = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    required_skills = models.TextField()
    type = models.CharField(max_length=255, null=True, blank=True)
    job_time_posted = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
