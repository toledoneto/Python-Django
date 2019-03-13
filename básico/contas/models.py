from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 100)
	dt_creation = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'Categories'

	# vai alterar como aparece na cx de seleção do front
	def __str__(self):
		return self.name
			

class Transaction(models.Model):
	date = models.DateTimeField() # sem o valor de param, o user poderá escolher pelo front já disponibilziado pelo Django
	description = models.CharField(max_length = 200)
	value = models.DecimalField(max_digits = 7, decimal_places = 2)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	details = models.TextField(null = True, blank = True)

	def __str__(self):
		return self.description
		