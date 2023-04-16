from django.contrib import admin
from .models import GlassType, Client, GlassDePres, GlassDeLoin, ProgressifDeLoin, ProgressifDePres, Order, LentilType, Lentil, PhotoClient, Menture, SaleSummary
from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.admin import SimpleListFilter
from business.models import Magasin

class HasReste(SimpleListFilter):
    title = "Reste" 
    parameter_name ="reste"
        # return Product.objects.filter(photos=True)
    def lookups(self, request, model_admin):
        return (
            ('true', 'Yes'),
            ('false', 'No')
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'true':
            return Order.objects.filter(rest__gt=0)
        elif self.value().lower() == 'false':
            return Order.objects.filter(rest=0)

class HasProgressif(SimpleListFilter):
    title = "Progressif" 
    parameter_name ="prog"
        # return Product.objects.filter(photos=True)
    def lookups(self, request, model_admin):
        return (
            ('true', 'Yes'),
            ('false', 'No')
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'true':
            return Order.objects.filter(de_loin_progressifs__isnull=False).distinct()
        elif self.value().lower() == 'false':
            return Order.objects.filter(de_loin_progressifs__isnull=True).distinct()

class HasLentilles(SimpleListFilter):
    title = "Lentilles" 
    parameter_name ="lent"
        # return Product.objects.filter(photos=True)
    def lookups(self, request, model_admin):
        return (
            ('true', 'Yes'),
            ('false', 'No')
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'true':
            return Order.objects.filter(lentilles__isnull=False).distinct()
        elif self.value().lower() == 'false':
            return Order.objects.filter(lentilles__isnull=True).distinct()
        
def order_pdf(obj):
    url = reverse('core:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}" print>Imprimer</a>')
order_pdf.short_description = 'Reçu Client'

def admin_pdf(obj):
    url = reverse('core:admin_bill_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}" print>Imprimer</a>')
admin_pdf.short_description = 'Reçu Magasin'

class LentiltInline(admin.TabularInline):
    
    model = Lentil
    fields = ('order', 'lentil_type', 'eye_choice', 'spheric_glass', 'spher', 'cyl', 'axe','rayon', 'diametre',  'brand', 'note', )
    extra = 2
    verbose_name = "Lentille"
    verbose_name_plural = "Lentille"

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    verbose_name = "Order"
    verbose_name_plural = "Order"

class MenturetInline(admin.TabularInline):
    model = Menture
    extra = 0
    verbose_name = "Menture"
    verbose_name_plural = "Menture"

class PhotoClienttInline(admin.TabularInline):
    model = PhotoClient
    extra = 0
    verbose_name = "Photo"
    verbose_name_plural = "Photo"


class GlassDePrestInline(admin.TabularInline):
    model = GlassDePres
    extra = 2
    verbose_name = "Vision De Prés"
    verbose_name_plural = "Vision De Prés"
    # exclude=('product',)
    # search_fields = ('id', 'spher', 'cyl', )
    # autocomplete_fields = [ 'spher', 'cyl']

class GlassDeLointInline(admin.TabularInline):
    model = GlassDeLoin
    extra = 2
    verbose_name = "Vision De Loin"
    verbose_name_plural = "Vision De Loin"


class ProgressifDeLoinInline(admin.TabularInline):
    model = ProgressifDeLoin
    extra = 2
    verbose_name = "Vision De Loin (Progressif)"
    verbose_name_plural = "Vision De Loin (Progressif)"

class ProgressifDePresInline(admin.TabularInline):
    model = ProgressifDePres
    extra = 2
    verbose_name = "Vision De Pres (Progressif)"
    verbose_name_plural = "Vision De Pres (Progressif)"

class GlassDePresAdmin(admin.ModelAdmin):
    list_display = ('id','order', 'eye_choice', 'spheric_glass', 'spher', 'cyl', 'axe', )
    list_display_links = ('id','order' )
    search_fields = ('id', 'order', )

    list_per_page = 40
    save_as = True

    # inlines=[GlasstInline, ProgressifInline]
# LentilType
class LentilTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id','name' )
    search_fields = ('id', 'name', )

    list_per_page = 40
    save_as = True


class GlassTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id','name' )
    search_fields = ('id', 'name', )
    list_per_page = 40
    save_as = True

class OrderAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.magasin:
            return qs.filter(client__magasin=request.user.magasin)
        elif request.user.is_superuser:
            return qs
        else:
            return qs.none()
    save_on_top = True
        
    list_display = ('id', 'client',  'date', 'total', 'rest', 'versement', 'paid','ordonnance_return',admin_pdf, order_pdf)
    autocomplete_fields = ['client',]
    exclude = ('number',)
    list_display_links = ('id','client', )
    search_fields = ('id', 'client__name')
    list_filter = ('ordonnance_return', 'client__magasin','date','paid', HasReste, HasProgressif, HasLentilles)
    save_as = True
    inlines=[GlassDeLointInline, GlassDePrestInline,  ProgressifDeLoinInline, ProgressifDePresInline, LentiltInline, MenturetInline, PhotoClienttInline]

class ClientAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.magasin:
            return qs.filter(magasin=request.user.magasin)
        elif request.user.is_superuser:
            return qs
        else:
            return qs.none()
    def save_model(self, request, obj, form, change):
        magasin_principale = Magasin.objects.filter(principale=True).first()
        user = request.user
        print('THE USER', user)
        if not obj.magasin:
            obj.magasin = user.magasin or magasin_principale or None
        super().save_model(request, obj, form, change)

    list_display = ('id','magasin', 'name', 'age', 'prenom', 'phone',  'doctor', )

    list_display_links = ('id','name' )
    list_filter = ('magasin',)
    search_fields = ('id', 'name', 'phone',)
    save_as = True
    inlines=[OrderInline]


import datetime
from django.db.models import Sum
from django.db.models import Count
@admin.register(SaleSummary)
class SaleSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    # date_hierarchy = 'created'

    def get_order_qs(self, request):
        today = datetime.date.today()
        # return Order.objects.filter(created__date=today)
        return Order.objects.all()

    def get_spher_qs(self, request):
        orders = self.get_order_qs(request)
        return GlassDePres.objects.filter(order__in=orders).distinct()

    # def get_sales_data(self, request):
    #     orders = self.get_order_qs(request)
    #     spher_values = self.get_spher_qs(request)
    #     # depres = GlassDePres.objects.filter(order__in=orders).distinct()

    #     sales_data = {}

    #     for spher in spher_values:
    #         spher_sales_data = {}
    #         for type_de_verre in type_de_verre_values:
    #             sales = GlassDePres.objects.filter(order__in=orders, spher=spher, type_de_verre=type_de_verre)
    #             total_sales = sales.aggregate(total_sales=Sum('order__versement'))['total_sales'] or 0
    #             spher_sales_data[type_de_verre.name] = total_sales
    #         sales_data[spher] = spher_sales_data
    #     return sales_data, spher_values, type_de_verre_values
    
    def changelist_view(self, request, extra_context=None):
        type_de_verre_values = self.get_spher_qs(request).values('type_de_verre__name', 'type_de_verre__id').annotate(tpcount=Count('type_de_verre')).order_by('type_de_verre')
        print('type_de_verre_values', type_de_verre_values)
        corrections = self.get_spher_qs(request).order_by('type_de_verre')
        # sales_data, spher_values, type_de_verre_values = self.get_sales_data(request)
        context = {
            'type_de_verre_values': type_de_verre_values,
            'corrections': corrections,
        }
        return super().changelist_view(request, extra_context=context)



    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #     try:
    #         qs = response.context_data['cl'].queryset
    #         print('THE QS', qs)
    #     except (AttributeError, KeyError):
    #         return response

    #     metrics = {
    #         'total': "23",
    #         'total_sales': "65000",
    #     }

    #     response.context_data['summary'] = qs.values('de_pres_glasses__type_de_verre').order_by('-created')
    #     print('response.context_dat', response.context_data['summary'])
    #     return response





admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(GlassType, GlassTypeAdmin)
admin.site.register(LentilType, LentilTypeAdmin)


admin.site.register(GlassDePres, GlassDePresAdmin)


