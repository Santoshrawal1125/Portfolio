from django.shortcuts import render
from django.views.generic import View
from .models import *


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
