from django.urls import path
from .views import index_view, admin_order_pdf, admin_bill_pdf

app_name= 'core'

urlpatterns = [
    path('', index_view, name="index"),
    path('pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),
    path('admin-bill/<int:order_id>/', admin_bill_pdf, name='admin_bill_pdf'),
]
