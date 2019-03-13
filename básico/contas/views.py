# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Transaction
from .form import TransactionForm

import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html')

def listDB(request):
	data = {}

	# objects é um manager nativo do Django que permite ter funções básicas de DB
	data['transactions'] = Transaction.objects.all()
	return render(request, 'contas/list.html', data)

def create_transaction(request):
	form = TransactionForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('url_listAllTransaction')

	return render(request, 'contas/form.html', {'form': form})

def update(request, pk):
	trasaction = Transaction.objects.get(pk = pk)
	# preenchemos o form com o que vier do DB OU
	# com o que o user passou através de 'instance'
	form = TransactionForm(request.POST or None, instance = trasaction)

	if form.is_valid():
		form.save()
		return redirect('url_listAllTransaction')

	return render(request, 'contas/form.html', {'form': form, 'transaction': trasaction})

def delete(request, pk):
	trasaction = Transaction.objects.get(pk = pk)
	trasaction.delete()
	return redirect('url_listAllTransaction')