from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product
from django.views.generic import ListView, View


class HomeView(ListView):
    model = Product
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactsView(View):
    template_name = 'contacts.html'

    def get(self, request):
        context = {"title": 'Контакты'}
        return render(request, self.template_name, context)

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductDetailsView(View):
    template_name = 'product_details.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {"product": product, "title": f"Товар №{pk}"}
        return render(request, self.template_name, context)


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()