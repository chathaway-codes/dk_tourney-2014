from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import FilteredSelectMultiple

from tournament.models import Player, Platform, Game, Computer

class PlayerForm(ModelForm):
    games = forms.ModelMultipleChoiceField(queryset=Game.objects.all(), widget=FilteredSelectMultiple("Games", is_stacked=False), required=False)
    platforms = forms.ModelMultipleChoiceField(queryset=Platform.objects.all(), widget=FilteredSelectMultiple("Platforms", is_stacked=False), required=False)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerForm, self).form_valid(form)

    class Meta:
        model = Player
        exclude = ('user',)

class ComputerForm(ModelForm):
    def form_valid(self, form):
        form.instance.player = self.request.user.player
        return super(ComputerForm, self).form_valid(form)

    class Meta:
        model = Computer
        exclude = ('player',)
