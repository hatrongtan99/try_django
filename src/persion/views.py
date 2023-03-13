from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


def product_create_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)


def product_raw_create_view(request):
    form = RawProductForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data:
            Product.objects.create(**form.cleaned_data)
            form = RawProductForm()
    context = {
        "form": form
    }
    return render(request, "products/raw_product_create.html", context)


def product_list_view(request):
    obj = Product.objects.all()
    context = {
        "object": obj
    }
    return render(request, "products/product_list.html", context)


def product_detail_view(request, id):
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    # context = {
    #     "product": obj
    # }
    # return render(request, "products/product_detail.html", context)

    obj = get_object_or_404(Product, id=id)

    context = {
        "product": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = Product.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context = {
        "product": obj
    }
    return render(request, "products/product_delete.html", context)
