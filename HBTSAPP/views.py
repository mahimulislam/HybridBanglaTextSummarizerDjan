from django.shortcuts import render
from .forms import ContactForm
import re
from . import first
from . import DocClassifierAll
from django.template.defaultfilters import linebreaks
from polyglot.text import Text, Word
import glob
from polyglot.text import Text, Word
import errno
import os
from subprocess import Popen, PIPE, STDOUT
from django.template.response import TemplateResponse
def home(request):
    username = request.POST.get('usrname')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'HBTSAPP/index.html', {'form': form})

def stringss(ts,big):
    ts+=big
def hi(request, template_name="HBTSAPP/index.html"):
    textarea = request.POST.get('tes')
    tk=""
    pk=""
    if(textarea==None):
        print("Not")
    else:
        pk=DocClassifierAll.main(textarea)
        tk=textarea
        print(pk)
    return render(request, template_name, {'title': pk,'title1': tk})