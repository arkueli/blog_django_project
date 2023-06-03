from parsers.views import RunTimesJobsParser
from django.urls import path, include

urlpatterns = [
    path('run_times_jobs_parser/', RunTimesJobsParser.as_view(), name='run_times_jobs_parser'),
]