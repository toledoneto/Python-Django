from django.forms import ModelForm
from .models import Clients


class ClientsForm(ModelForm):
	class Meta:
		model = Clients
		fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']