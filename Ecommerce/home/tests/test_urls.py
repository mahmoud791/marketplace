from django.test import SimpleTestCase
from django.urls import resolve,reverse
from home.views import homePage,user_profile,checkout,product_detail,cart,search


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):

        url = reverse('home')
        self.assertEquals(resolve(url).func,homePage)

    def test_user_profile_url_is_resolved(self):

        url = reverse('profile')
        self.assertEquals(resolve(url).func,user_profile)

    def test_cart_url_is_resolved(self):

        url = reverse('cart')
        self.assertEquals(resolve(url).func,cart)


    def test_checkout_url_is_resolved(self):

        url = reverse('checkout')
        self.assertEquals(resolve(url).func,checkout)

    def test_Product_detail_url_is_resolved(self):

        url = reverse('product_detail',args=['some-slug'])
        self.assertEquals(resolve(url).func,product_detail)

    def test_search_url_is_resolved(self):

        url = reverse('search')
        self.assertEquals(resolve(url).func,search)



        

        

