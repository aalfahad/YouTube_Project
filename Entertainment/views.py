from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Channel,Video
from .forms import ChannelForm,VideoForm
from django.contrib.auth.models import User
# Create your views here.

def channel_list(request):
