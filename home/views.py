from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.http import FileResponse, HttpResponseNotFound
from django.http import HttpResponse
from django.conf import settings
import os


# Create your views here.

class Base(View):
    views = {}


class HomeView(Base):

    def get(self, request):
        return render(request, 'index.html', self.views)

    def post(self, request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            data = Contact.objects.create(

                name=name,
                email=email,
                message=message

            )
            data.save()

        return render(request, 'index.html', self.views)


class ProjectDetailView(Base):

    def get(self, request):
        return render(request, 'project.html', self.views)


def download_cv(request):
    cv_path = os.path.join(settings.MEDIA_ROOT, 'cv.pdf')  # Adjust the file name accordingly

    if os.path.exists(cv_path):
        with open(cv_path, 'rb') as cv_file:
            response = HttpResponse(cv_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
            return response
    else:
        return HttpResponseNotFound("CV not found.")
