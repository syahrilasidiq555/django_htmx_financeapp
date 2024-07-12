from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import TransactionFilter

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')


@login_required
def transaction_list(request):
    transaction_filter = TransactionFilter(
        request.GET,
        queryset = Transaction.objects.filter(user=request.user).select_related('category')
    )

    context = {
        'filter': transaction_filter
    }
    if request.htmx:
        return render(request, 'tracker/partials/transactions-container.html', context)

    return render(request, 'tracker/transactions_list.html', context)