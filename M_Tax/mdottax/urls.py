from django.urls import path

from .import views


urlpatterns = [


#websites Main Pages
path('',views.home, name='home'),
    
path('about_us',views.about_us, name='about_us'),

path('bookeeping_service',views.bookeeping_service, name='bookeeping_service'),

path('business_tax_service',views.business_tax_service, name='business_tax_service'),

path('income_tax_service',views.income_tax_service, name='income_tax_service'),


path('business_formation_and_ITIN',views.business_formation_and_ITIN, name='business_formation_and_ITIN'),


path('accounting_taxation_outsourcing',views.accounting_taxation_outsourcing, name='accounting_taxation_outsourcing'),

path('sales_and_use_tax_Service',views.salestax, name='sales_and_use_tax_Service'),


path('error',views.error, name='error'),




]