from django import forms


class ItemPedidoForm(forms.Form):
    produto_id = forms.CharField(label='Id Produto', max_length=100)
    quantidade = forms.IntegerField(label='Quantidade')
    desconto = forms.DecimalField(label='Desconto', max_digits=7, decimal_places=2)
