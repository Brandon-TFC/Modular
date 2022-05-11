from django.db import models
from django.db.models.deletion import CASCADE
from orden.comun import OrdenStatus
from users.models import User
from products.models import Product
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import m2m_changed
import uuid
# Create your models here.
#Se crean la base de datos de los siguientes datos
class Cart(models.Model):
    cart_id = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
    )
    user = models.ForeignKey(
        User,
        null=True, 
        blank=True,
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(Product, through='CartProduct') #Le decimos que los productos van a tener que estar de muchos a muchos
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

    """
    --Subtotalé calculaté--

    import decimal
    
    FEE = 0.01 -- Comission example.

    def update_totals(self):
        self.update_subtotal()
        self.update_total()

    def update_subtotal(self):
        self.subtotal = sum([product.price for product in self.products.all()])
        self.save()
    
    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()
    """
    
    def update_totals(self):
        #self.update_subtotal()
        self.update_total()
        
        if self.orden:
            self.orden.update_total()

    def update_total(self):
        #self.total = sum([product.price for product in self.products.all()]) 
        self.total = sum([
            i.quantity * i.product.price for i in self.product_related()
        ])
        self.save()

    def product_related(self):
        return self.cartproduct_set.select_related('product')

    @property #Decorador para la funcion orden
    def orden(self):
        return self.orden_set.filter(status=OrdenStatus.CREATED).first()#Una vez la orden este creada va a retornar a la status de la orden


class CartProductManager(models.Manager):
    def crearActualizar(self, cart, product, quantity=1):
        object, created = self.get_or_create(cart=cart, product=product) #Almaacenamos los productos en un objeto
        if not created: #Si no se crea los objetos en el producto
            quantity = object.quantity + quantity #Le asignamos una cantidad nula en este caso 0
        
        object.update_quantity(quantity) #Si se agrega mas de un producto se actualiza
        return object #Regresamos al objeto si deseamos agregar mas

#Base de datos para poder almacenar los productos
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    object = CartProductManager() #Le asignamos object la funcion para que se haga mas facil mandar a llamarla

#Guardamos los updates de las cantidades que fallamos almacenando
    def update_quantity(self, quantity=1):
        self.quantity = quantity
        self.save()

#Funcion para mostrar el set del cart id
def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id: #Si no esta en una instancia pasamos a declararla
        instance.cart_id = str(uuid.uuid4()) #Le asignamos a instance una cadena donde se tendra que almacenar

#Funcion para almacenar los totales
def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear': #condicion para poder hacer ya sea add, remove, clear
        instance.update_totals() #Se hace un update de acorde a lo seleccionado

#Funcion post esto solo sera para ir actualizando el carro
def postActualizar(sender, instance, *args, **kwargs):
    instance.cart.update_totals() 


post_save.connect(postActualizar, sender=CartProduct)#Almacenamos lo del carro
pre_save.connect(set_cart_id, sender=Cart) #Presave por si se elimina algo del carro antes de pasar al pago
m2m_changed.connect(update_totals, sender=Cart.products.through) #Con esto conectamos los productos al carro