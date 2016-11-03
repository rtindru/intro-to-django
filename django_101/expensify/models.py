from django.contrib.auth.models import User
from django.db import models


TRANSACTION_TYPES = (
    ('CR', 'Credit'),
    ('DE', 'Debit'),
)


class Transaction(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    type = models.CharField(choices=TRANSACTION_TYPES, default='DE', max_length=3)
    description = models.TextField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}, {}-{}".format(self.user, self.amount, self.type)

