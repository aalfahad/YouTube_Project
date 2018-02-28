from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Channel,Video
from .forms import ChannelForm,VideoForm
from django.contrib.auth.models import User
# Create your views here.

def channel_list(request):
	channels = Channel.objects.all()
	context = {
	"channels": channels,
	}
	return render(request, 'channel_list.html', context)

def channel_delete(request, channel_id):
	Channel.objects.get(id= channel_id).delete()
	return redirect('channel_list')

def channel_create(request):
	form = ChannelForm()
	if request.method == "POST":
		form = ChannelForm(request.POST)
		if form.is_valid():
			channel= form.save(commit= False)
			channel.creator = request.user
			channel.save()
			return redirect("channel_list")
	context = {
		"form" : form,
	}
	return render(request,'channel_create.html',context)

def channel_udate(request, channel_id):
	channel_obj = Channel.objects.get(id= channel_id)
	form = ChannelForm(instance= channel_obj)
	if request.method == "POST":
		form = ChannelForm(request.POST,instance=channel_obj)
		if form.is_valid():
			form.save()
			return redirect('channel_detail',channel_id=channel_obj.id)
	context = {
		"form" : form,
		"channel": channel_obj,
	}
	return render(request,'channel_update.html',context)