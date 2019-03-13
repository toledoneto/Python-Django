from django.contrib import admin
from .actions import nfe_emitida, nfe_nao_emitida
from .models import ItemDoPedido, Venda


# Register your models here.
class ItemPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    autocomplete_fields = ("pessoa",)
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'pessoa', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    inlines = [ItemPedidoInline]

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


admin.site.register(ItemDoPedido)
admin.site.register(Venda, VendaAdmin)
