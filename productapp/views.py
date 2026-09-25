from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductDetails
# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):

    if request.method == "POST":

        productName = request.POST.get("productName")
        category = request.POST.get("category")
        brand = request.POST.get("brand")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        description = request.POST.get("description")
        date = request.POST.get("date")
        image = request.FILES.get("image")

        availability = request.POST.get("availability") == "available"

        ProductDetails.objects.create(
            productName=productName,
            category=category,
            brand=brand,
            price=price,
            quantity=quantity,
            description=description,
            date=date if date else None,
            image=image,
            availability=availability
        )

        return redirect("list")

    return render(request, "register.html")

    
def list(request):
    products = ProductDetails.objects.all().order_by("-id")

    return render(request,"list.html",{"products": products})
    
def update(request, product_id):
    product = get_object_or_404(ProductDetails,id=product_id)

    if request.method == "POST":

        product.productName = request.POST.get("productName")
        product.category = request.POST.get("category")
        product.brand = request.POST.get("brand")
        product.price = request.POST.get("price")
        product.quantity = request.POST.get("quantity")
        product.description = request.POST.get("description")

        date = request.POST.get("date")

        product.date = date if date else None

        
        product.availability = (
            request.POST.get("availability") == "available"
        )

        new_image = request.FILES.get("image")

        if new_image:
            product.image = new_image

        product.save()

        return redirect("list")

    return render(request,"update.html",{"product": product})

def delete(request, product_id):

    product = get_object_or_404(
        ProductDetails,
        id=product_id
    )

    if request.method == "POST":

        product.delete()

        return redirect("list")

    return render(request,"delete.html",{"product": product})