from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR vistING.",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context

class ProductsPageView(TemplateView):
    template_name= "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["products"] = [
            {"name": "Phone", "price": 100},
            {"name": "Laptop", "price": 199.99},
            {"name": "Keyboard", "price": 40},
            {"name": "Monitor", "price": 69.99},
        ]
        return context
        
        
    

