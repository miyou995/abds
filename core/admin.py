from django.contrib import admin
from .models import GlassType, Client, GlassDePres, GlassDeLoin, ProgressifDeLoin, ProgressifDePres, Order, LentilType, Lentil, PhotoClient, Menture
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
    list_display = ('id', 'client',  'date', 'total', 'rest', 'versement', 'paid','ordonnance_return',admin_pdf, order_pdf)
    autocomplete_fields = ['client',]

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


admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(GlassType, GlassTypeAdmin)
admin.site.register(LentilType, LentilTypeAdmin)


admin.site.register(GlassDePres, GlassDePresAdmin)

