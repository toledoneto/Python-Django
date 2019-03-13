from django.forms import ModelForm
from .models import Transaction

# Create the form class.
class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
		fields = ['date', 'description', 'value', 'details', 'category']