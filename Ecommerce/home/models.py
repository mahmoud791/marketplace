from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.









class Product (models.Model):
    CATEGORY=(
        ('clothes','clothes'),
        ('shoes','shoes'),
        ('watches','watches'),
        ('laptops','laptops'),
        ('mobile phones','mobile phones'),
        ('headphones/headsets','headphones/headsets'),
        ('perfumes/deodrants','perfumes/deodrants'),
        ('accessories','accessories'),
        ('kid toys','kid toys'),
        ('HouseHold', 'HouseHold'),


    )


    name = models.CharField(max_length=200,null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    category = models.CharField(max_length=64,choices=CATEGORY,null=True)
    seller = models.ForeignKey(User, related_name='seller',null=True,on_delete=models.CASCADE)
    

    class Meta:
        unique_together = ('name','slug')

    def __str__(self):
        return self.name

    
    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0

class product2 (models.Model):
    product = models.OneToOneField(Product,null=True,on_delete=models.CASCADE)
    manufacturer_name = models.CharField(max_length=200,null=True)
    current_location = models.CharField(max_length=200,null=True)
    origin_country = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Product)
def create_product2(sender, instance, created, **kwargs):
    if created:
        product2.objects.create(product=instance)


@receiver(post_save, sender=Product)
def save_product2(sender, instance, **kwargs):
    instance.product2.save()  




class Order(models.Model):
    customer = models.ForeignKey(User,null=True,on_delete = models.SET_NULL)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.transaction_id)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([1 for item in orderitems])
        return total

class order2(models.Model):
    order = models.OneToOneField(Order,null=True,on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipping_company = models.CharField(max_length=200,null=True)

@receiver(post_save, sender=Order)
def create_order2(sender, instance, created, **kwargs):
    if created:
        order2.objects.create(order=instance)


@receiver(post_save, sender=Order)
def save_order2(sender, instance, **kwargs):
    instance.order2.save()  




class OrderItem(models.Model):
    order = models.ForeignKey(Order,null=True,blank=True,on_delete = models.SET_NULL)
    product = models.ForeignKey(Product,null=True,blank=True,on_delete = models.SET_NULL)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total

class orderitem2(models.Model):
    orderitem = models.OneToOneField(OrderItem,null=True,on_delete=models.CASCADE)
    batch_no = models.IntegerField(null=True)
    expiration_date = models.DateField(auto_now_add=True)

@receiver(post_save, sender=OrderItem)
def create_orderitem2(sender, instance, created, **kwargs):
    if created:
        orderitem2.objects.create(orderitem=instance)


@receiver(post_save, sender=OrderItem)
def save_orderitem2(sender, instance, **kwargs):
    instance.orderitem2.save()  


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)




def create_slug(instance,new_slug=None):
    slug=slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug



def pre_save_product_reciever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
  




pre_save.connect(pre_save_product_reciever,sender=Product)