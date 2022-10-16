from contextlib import nullcontext
from doctest import BLANKLINE_MARKER
from tkinter import Widget
from tokenize import blank_re
from typing_extensions import Required
from xml.dom.minidom import Attr
from django import forms
from django.forms import Textarea
from pkg_resources import require

from .models import Post

from django.contrib.auth import get_user_model

User = get_user_model()


class CreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text', 'group', ]
        Widget = {
            'text': forms.Textarea(attrs={
                    'class': 'form-input',
                }
            ),
            'group': forms.ChoiceField(required=False, )
        }