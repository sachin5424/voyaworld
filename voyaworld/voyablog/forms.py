from django import forms
from voyablog.models import Blog,Profile
from django.forms import ModelForm, Textarea, TextInput,Select,FileInput



class ContactForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
            'Blog_title': TextInput(attrs={
                'autocomplete': 'off'}),
            'Blog_title': TextInput(attrs={
                "class": "bg-white rounded border border-red-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4 mt-0"}),
            'img': FileInput(attrs={
                "class": "bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4"}),
            'cat': Select(attrs={
                 "class": "bg-white rounded border border-gray-400 focus:outline-none h-12 focus:border-indigo-500 text-base px-4 py-2 mb-4 resize-none w-30"}),
            'dec': Textarea(attrs={
                "class": "bg-white rounded border border-gray-400 focus:outline-none h-32 focus:border-indigo-500 text-base px-4 py-2 mb-4 resize-none w-500 'autocomplete': 'off'" }),
        }

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','Profile_image','phone_no','skills']
        widgets = {
            'name': TextInput(attrs={
                "class": "control-form bg-black"}),

        }


