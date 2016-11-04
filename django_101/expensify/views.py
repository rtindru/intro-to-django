from django.shortcuts import render, redirect

from expensify.models import Transaction
from expensify.forms import TransactionForm


def transaction_list(request):
    transactions = Transaction.objects.all()
    balance = sum([x.amount for x in transactions])
    return render(request, 'transactions.html', {'transactions': transactions, 'balance': balance})


def transaction_form(request):
    if request.method == 'GET':
        form = TransactionForm()
        return render(request, 'transaction_form.html', {'form': form})
    elif request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            return redirect('transaction_list')
        else:
            return render(request, 'transaction_form.html', {'form': form})
