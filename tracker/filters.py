import django_filters
from tracker.models import Transaction, Category


class TransactionFilter(django_filters.FilterSet):
    transaction_type = django_filters.ChoiceFilter(
        choices=Transaction.TRANSACTION_TYPE_CHOICES,
        field_name="type",
        lookup_expr="iexact",
        empty_label="Any",
    )