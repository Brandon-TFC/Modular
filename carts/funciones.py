from .models import Cart

def funcionCarrito(request):
    user = request.user if request.user.is_authenticated else None 
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first()
    if cart is None: #Debemos tener una login para agregar al carro
        cart = Cart.objects.create(user=user) #Caso de que no se mandara a crear uno
    
    if user and cart.user is None: 
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id #Una vez vayamos al carro se agregara una session
    
    return cart


def deleteCart(request): #Borrar lo que este en el carro
    request.session['cart_id'] = None