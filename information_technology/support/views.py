# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from support.forms import Contact_Form
# Create your views here.

def Contact_Us(request):
    form= Contact_Form()
    # template_name = 'support/support_form.html'
    if request.method == "POST":
        form = Contact_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = Contact_Form()
        else:
            print('ERROR')

    return render(request, 'support/support_form.html',{'form':form})
