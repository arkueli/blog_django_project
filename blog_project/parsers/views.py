import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from parsers.models import Parser, Job
from rest_framework import generics
from rest_framework.response import Response
from parsers.serializers import ParserSerializer

# Create your views here.

class RunTimesJobsParser(generics.GenericAPIView):
    serilizer_class = ParserSerializer
    JOB = "timesjobs"
    TARGET_URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="


    def get_content(self):
        return requests.get(self.TARGET_URL).text

    def parser(self):
        content = self.get_content()
        soup = BeautifulSoup(content,'lxml')
        job_list = soup.find('ul', {'class': 'new-joblist'}).find_all('li', {'class': 'clearfix'})
        data = []
        for job in job_list:
            work_type = job.find('span', {'class': 'sim-posted'}).find('span', {'class': 'jobs-status'})
            data.append({
                'title': job.find('h2').get_text(strip=True),
                'company': job.find('h3').get_text(strip=True),
                'years_of_experience': job.find('ul', {'class': 'top-jd-dtl clearfix'}).find_all('li')[0].get_text(strip=True).replace('card_travel', ''),
                'location': job.find('ul', {'class': 'top-jd-dtl clearfix'}).find_all('li')[1].get_text(strip=True).replace('location_on', ''),
                'description': job.find('ul', {'class': 'list-job-dtl clearfix'}).find_all('li')[0].get_text(strip=True).replace('Job Description:', ''),
                'required_skills': job.find('ul', {'class': 'list-job-dtl clearfix'}).find_all('li')[1].get_text(strip=True).replace('KeySkills:', ''),
                'type': job.find('span', {'class': 'sim-posted'}).find('span', {'class': 'jobs-status'}).get_text(strip=True) if work_type else None,
                'job_time_posted': job.find('span', {'class': 'sim-posted'}).find_all('span')[-1].get_text(strip=True),
            })
        return data
    
    def get(self, request, *args, **kwargs):
        try:
            parser_name, _ = Job.objects.get_or_create(name=self.JOB)
            for obj in self.parser():
                Parser.objects.get_or_create(name=parser_name, **obj)
            return Response({"success": "data successfully added!"})
        except Exception as e:
            return Response({"error": str(e)})
