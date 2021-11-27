from django.core.paginator import Paginator
from .models import CustomerContactForm, CustomerBillingForm, CustomerShippingForm


# Number of posts per page
CUSTOMER_PER_PAGE = 10


def paginate_customers(request, customers):
    """
    Paginating customers
    """
    paginator = Paginator(customers, CUSTOMER_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def save_customer(request, customer):
    """
    Save customer to database
    """
    contact = CustomerContactForm(request.POST or None, instance=customer)
    billing = CustomerBillingForm(request.POST or None, instance=customer)
    shipping = CustomerShippingForm(
        request.POST or None, instance=customer)
    if contact.is_valid and billing.is_valid and shipping.is_valid:
        contact.save()
        billing.save()
        shipping.save()
