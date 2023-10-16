from django import forms
from .models import Song
class RatingForm(forms.Form):
    nick = forms.CharField(
        label='Nick',
        max_length=60,
        required=True,  # Ustal jako wymagane, jeśli chcesz, aby użytkownik musiał wprowadzić nick
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    rating = forms.ChoiceField(
        label='Ocena',
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
        widget=forms.RadioSelect(),
    )

#class DodajPiosenkiForm(forms.Form):
#    plik_tekstowy = forms.FileField()
class DodajPiosenkiForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['jezyk']
    jezyk = forms.CharField(max_length=50, required=True, help_text="Wprowadź kategorię piosenek")

    plik_tekstowy = forms.FileField(required=True, label="Plik tekstowy z piosenkami")
