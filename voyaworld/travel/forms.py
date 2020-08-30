from django import forms
from travel.models import ContactAdd
from django.forms import ModelForm, Textarea, TextInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactAdd
        fields = "__all__"
        widgets = {
            'contact_name': TextInput(attrs={
                "class": "bg-white rounded border border-red-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4 mt-0"}),
            'contact_email': TextInput(attrs={
                "class": "bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4"}),
            'contact_msg': Textarea(attrs={
                "class": "bg-white rounded border border-gray-400 focus:outline-none h-32 focus:border-indigo-500 text-base px-4 py-2 mb-4 resize-none w-500"}),

        }

