from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
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
    

class Order(models.Model):
    customer = models.ForeignKey(User,null=True,on_delete = models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
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
        total=sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order,null=True,blank=True,on_delete = models.SET_NULL)
    product = models.ForeignKey(Product,null=True,blank=True,on_delete = models.SET_NULL)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,null=True,on_delete = models.SET_NULL)
    order = models.ForeignKey(Order,null=True,blank=True,on_delete = models.SET_NULL)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address




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