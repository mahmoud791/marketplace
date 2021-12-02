from django.test import TestCase
from home.models import Product,User,ProductReview

class TestModels(TestCase):

    
    def setUp(self):

        
        

        self.product1 = Product.objects.create(
            name='product 1',
            description='test_product',
            price=120,
            category='shoes',
            amount=1
        )

        self.user1 = User.objects.create(
            username='user1',
            password='qwqwqwqw',
            email='www.@example.com'
        )
        self.user2 = User.objects.create(
            username='user2',
            password='qwqwqwqw',
            email='www.@example.com'
        )

        

    def test_product_is_assigned_slug_on_creation(self):
        self.assertEquals(self.product1.slug,'product-1')


    def test_get_rating(self):
        

        self.product1 = Product.objects.create(
            name='product 1',
            description='test_product',
            price=120,
            category='shoes',
            amount=1
        )

        

        ProductReview.objects.create(
            user=self.user1,
            product=self.product1,
            content='sometext',
            stars=5
        )
        ProductReview.objects.create(
            user=self.user2,
            product=self.product1,
            content='sometext',
            stars=1
        )

        self.assertEquals(self.product1.get_rating(),3.0)


        



    



