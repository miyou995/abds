from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from .models import Order
from business.models import Business
from business.models import Magasin
# Create your views here.
def index_view(request):
    return redirect('admin:index')



@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=order_{order.id}.pdf"
    # business = Business.objects.first()
    business = order.client.magasin or  Business.objects.first()
    context = {
        "order": order, 
        "business": business,
    }
    html = render_to_string("order_pdf.html", context)
    # stylesheets=[weasyprint.CSS(str(configs.STATIC_ROOT) + 'css/pdf.css' )]
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        response
    )
    return response

@staff_member_required
def admin_bill_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=admin_bill_{order.id}.pdf"
    user = request.user
    magasin_principale = Magasin.objects.filter(principale=True).first()

    business = order.client.magasin or  Business.objects.first()
    print('order.de_loin_glasses.count', order.de_loin_glasses.all())
    context = {
        "order": order, 
        "de_loins": order.de_loin_glasses.all(),
        "de_pres": order.de_pres_glasses.all(),
        "progressifs_de_loin": order.de_loin_progressifs.all(),
        "progressifs_de_pres": order.de_pres_progressifs.all(),
        "lentilles": order.lentilles.all(),
        "business": business,
    }
    html = render_to_string("admin_bill_pdf.html", context)
    # stylesheets=[weasyprint.CSS(str(configs.STATIC_ROOT) + 'css/pdf.css' )]
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        response
    )
    return response