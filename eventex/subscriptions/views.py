# encoding: utf-8
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from django.http.response import HttpResponseRedirect
from eventex.subscriptions.models import Subscription

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
        else:
            return render(request, 'subscriptions/subscription_form.html', 
                          {'form': form})
    else:
        return render(request, 'subscriptions/subscription_form.html', 
                   {'form': SubscriptionForm()})
