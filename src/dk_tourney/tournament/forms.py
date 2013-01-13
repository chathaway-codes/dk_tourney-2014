from django import forms
from django.forms import ModelForm

from tournament.models import Player

class PlayerForm(ModelForm):
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerForm, self).form_valid(form)

    class Meta:
        model = Player
        exclude = ('user',)
