from django.shortcuts import render
from carts.models import CartProduct
from products.models import Product
from .funciones import funcionCarrito
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import CartProduct


def cart(request):
    cart = funcionCarrito(request)#Le pasamos el request para  poder hacer cambios en el html 

    return render(request, 'carts/cart.html', { #Mostramos el carro
        'cart' : cart, #Le asignamos su variable asignada
    })

#Request para poder evitar errores 
def add(request):
    cart = funcionCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id')) #En caso de que suceda un error con el producto y con su llave principal se le mandara un 404
    quantity = int(request.POST.get('quantity', 1))
    #cart.products.add(product, through_defaults={'quantity' : quantity})
    product_cart = CartProduct.object.crearActualizar(cart=cart, product=product, quantity=quantity) #Le asignamos a la vista del carro

    return render(request, 'carts/add.html', { #Retornamos a los productos por si se desea agregar 
        'product' : product,
    })
#Quitar algun producto
def remove(request):
    cart = funcionCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id')) #Si el producto y la llave principal concuerdan se quita
    cart.products.remove(product) #Producto quitado
    return redirect('cart') #Regresamos a la vista del carro para verificar que ya se elimino el producto