from django import forms
from .models import Channel,Video

class ChannelForm(forms.ModelForm):
	class Meta:
		model = Channel
		fields = '__all__'
		exclude = ['subscribers']

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = '__all__'
		exclude = ['channel']
