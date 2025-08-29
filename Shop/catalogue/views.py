from django.shortcuts import render,redirect
from .models import Product
from .forms import Product_Form

def list_products(request):

    products=Product.objects.all()
    return render(request,"catalogue/product_list.html",
    {"products":products})

def product_detail(request,id):
    product =Product.objects.get(id=id)
    return render (request,"catalogue/product_detail.html",
    {"product":product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('catalogue:product_list')
        else:
            return render(request, "catalogue/product_form.html", {"form": form})
    else:
        form = Product_Form()
        return render(request, "catalogue/product_form.html", {"form": form})

def add_to_cart(request,id):
    product = Product.objects.get(id=id)
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })
    
    return render(request, 'catalogue/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def delete_cart(request, id):
    cart = request.session.get('cart',{})
    if str(id) in cart:
        del cart[str(id)]
        request.session['cart'] = cart
    return redirect('cart_detail')    