from django.shortcuts import render

from expensify.models import Transaction


def transaction_list(request):
    transactions = Transaction.objects.all()
    balance = sum([x.amount for x in transactions])
    return render(request, 'transactions.html', {'transactions': transactions, 'balance': balance})
