from django.shortcuts import render
from django.http import HttpResponse

# DRF imports
from rest_framework import generics
from .serializers import AppUserSerializer
from .models import MasterUser, TalentUser, VenueUser, Post


# --------------------------------- DRF Views ---------------------------------

class CreateAppUserView(generics.CreateAPIView):
    queryset = MasterUser.objects.all()
    serializer_class = AppUserSerializer


class ListAppUserView(generics.ListAPIView):
    queryset = MasterUser.objects.all()
    serializer_class = AppUserSerializer


# ------------------------------- Vanilla Views -------------------------------

def home_view(request, *args, **kwargs):
    return render(request, '_Base.html')
