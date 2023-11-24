from dataclasses import field
from logging import PlaceHolder
from django import forms

from django.forms import ModelForm
from .models import Checkout



class ShipForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['firstname', 'lastname','email','address','city','state', 'notes']
        widgets ={
            'firstname': forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600', 'PlaceHolder':'First Name'}),
            'lastname': forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600', 'placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600', 'placeholder':'Email'}),
            'address': forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600', 'placeholder':'Address'}),
            'state': forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600', 'placeholder':'State'}),
            'city': forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600', 'PlaceHolder':'City'}),
            'notes': forms.Textarea(attrs={'class':'flex items-center w-full px-4 py-3 text-sm border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-blue-600', 'PlaceHolder':'Notes for delivery', 'row': '4'}),
        }

