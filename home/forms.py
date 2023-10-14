from django import forms
from .models import UserReservation


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control text-white rounded-0 bg-transparent',
            'name': 'name',
            'placeholder': 'Name'
        })
    )

    email = forms.CharField(
        max_length=30,
        widget=forms.EmailInput(attrs={
            'type': 'email',
            'class': 'form-control text-white rounded-0 bg-transparent',
            'name': 'Email',
            'placeholder': 'Email'
        })
    )

    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control text-white rounded-0 bg-transparent',
            'name': 'subject',
            'placeholder': 'Subject'
        })
    )

    massage = forms.CharField(
        max_length=700,
        widget=forms.TextInput(attrs={
            'name': 'message',
            'id': '',
            'cols': '30',
            'rows':'4',
            'class': 'form-control text-white rounded-0 bg-transparent',
            'placeholder': 'Message'
        })
    )

    class Meta:
        model = UserReservation
        fields = ('name', 'email', 'subject', 'massage')
