from django import forms
from .models import Channel,Video

class ChannelForm(forms.ModelForm):
	class Meta:
		model = Channel
		exclude = ['creator']

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		exclude = ['channel']
