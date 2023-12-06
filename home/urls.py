from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('project', ProjectDetailView.as_view(), name='project'),
    path('download-cv/', download_cv, name='download_cv'),
]
