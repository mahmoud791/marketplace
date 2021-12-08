from django.test import TestCase,Client
from django.urls import reverse
from home.models import Product,Order,OrderItem,ProductReview,User
import json

class TestViews(TestCase):


    def setUp(self):
        self.client=Client()
        self.home_url = reverse('home')
        self.user_profile_url = reverse('profile')
        self.cart_url = reverse('cart')
        self.checkout_url = reverse('checkout')
        self.test_product_url = reverse('product_detail',args=['product_1'])
        self.search_url = reverse('search')


        Product.objects.create(
            name='product_1',
            description='testproduct',
            price=120,
            category ='shoes',
            
            
        )



    def test_homePage_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home/homePage.html')


    def test_cart_GET(self):
        response = self.client.get(self.cart_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home/cart.html')

    def test_checkout_GET(self):
        response = self.client.get(self.checkout_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home/checkout.html')

    def test_product_detail_GET(self):
        response = self.client.get(self.test_product_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home/product_detail.html')


