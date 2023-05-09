from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


from .models import Bar, City, Cuisine, Hotel, LocalFav, Mall, Museum, Monument, Restaurant, Route, Zoo


# Create your tests here.
class SichuanInfoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="tester", email="test@email.com", password="secret"
        )

        cls.route = Route.objects.create(
            route_name="C-M-L",
            route_detail="abc"
        )

        cls.city = City.objects.create(
            city_name="成都Chengdu",
            city_intro="abc",
            city_id=1
        )

        cls.hotel = Hotel.objects.create(
            hotel_tel="123",
            hotel_name="good",
            hotel_website="abc",
            hotel_cost_per_night="$20",

            city=cls.city
        )

        cls.bar = Bar.objects.create(
            attraction_address="v50",
            attraction_name="ab",
            attraction_website="kfc",
            attraction_introduction="abc",
            attraction_tel="123",
            attraction_cost="10",
            suggest_duration="3h",
            bar_id=1,

            city=cls.city
        )

        cls.cuisine = Cuisine.objects.create(
            cuisine_name="abc",
            cuisine_history="abc is good"
        )

        cls.localfav = LocalFav.objects.create(
            attraction_address="A",
            attraction_name="AB",
            attraction_website="abc",
            attraction_introduction="Intro",
            attraction_tel="123",
            attraction_cost="20",

            city=cls.city
        )

        cls.mall = Mall.objects.create(
            attraction_address="B",
            attraction_name="YZ",
            attraction_website="xyz",
            attraction_introduction="intro",
            attraction_tel="12345",
            attraction_cost="100",

            city=cls.city
        )

        cls.museum = Museum.objects.create(
            attraction_address="B",
            attraction_name="YZ",
            attraction_website="xyz",
            attraction_introduction="intro",
            attraction_tel="12345",
            attraction_cost="100",

            city=cls.city
        )

        cls.monument = Monument.objects.create(
            attraction_address="B",
            attraction_name="YZ",
            attraction_website="xyz",
            attraction_introduction="intro",
            attraction_tel="12345",
            attraction_cost="100",

            city=cls.city
        )

        cls.restaurant = Restaurant.objects.create(
            restaurant_tel="123",
            restaurant_name="KFC",
            restaurant_address="abc",
            restaurant_history="good",

            city=cls.city
        )

        cls.zoo = Zoo.objects.create(
            attraction_address="B",
            attraction_name="YZ",
            attraction_website="xyz",
            attraction_introduction="intro",
            attraction_tel="12345",
            attraction_cost="100",

            city=cls.city
        )

        # many-to-many relationships
        cls.bar.hotel.set([cls.hotel])
        cls.bar.route.set([cls.route])

        cls.city.route.set([cls.route])

        cls.cuisine.restaurant.set([cls.restaurant])

        cls.hotel.route.set([cls.route])

        cls.localfav.hotel.set([cls.hotel])
        cls.localfav.route.set([cls.route])

        cls.mall.hotel.set([cls.hotel])
        cls.mall.route.set([cls.route])

        cls.museum.hotel.set([cls.hotel])
        cls.museum.route.set([cls.route])

        cls.monument.hotel.set([cls.hotel])
        cls.monument.route.set([cls.route])

        cls.restaurant.hotel.set([cls.hotel])
        cls.restaurant.route.set([cls.route])

        cls.zoo.hotel.set([cls.hotel])
        cls.zoo.route.set([cls.route])

    # test model.py
    def test_system(self):
        # bar
        self.assertEqual(self.bar.attraction_address, "v50")
        self.assertEqual(self.bar.attraction_website, 'kfc')
        self.assertEqual(self.bar.attraction_name, 'ab')

        # city
        self.assertEqual(self.city.city_name, "成都Chengdu")
        self.assertEqual(self.city.city_intro, "abc")

        # cuisine
        self.assertEqual(self.cuisine.cuisine_history, "abc is good")
        self.assertEqual(self.cuisine.cuisine_name, "abc")

        # hotel
        self.assertEqual(self.hotel.hotel_tel, "123")
        self.assertEqual(self.hotel.hotel_name, "good")
        self.assertEqual(self.hotel.hotel_website, "abc")

        # localfav
        self.assertEqual(self.localfav.attraction_tel, "123")
        self.assertEqual(self.localfav.attraction_cost, "20")
        self.assertEqual(self.localfav.attraction_name, "AB")

        # mall
        self.assertEqual(self.mall.attraction_tel, "12345")
        self.assertEqual(self.mall.attraction_name, "YZ")
        self.assertEqual(self.mall.attraction_introduction, "intro")

        # museum
        self.assertEqual(self.museum.attraction_address, "B")
        self.assertEqual(self.museum.attraction_introduction, "intro")
        self.assertEqual(self.museum.attraction_name, "YZ")

        # monument
        self.assertEqual(self.monument.attraction_cost, "100")
        self.assertEqual(self.monument.attraction_website, "xyz")
        self.assertEqual(self.monument.attraction_tel, "12345")

        # restaurant
        self.assertEqual(self.restaurant.restaurant_name, "KFC")
        self.assertEqual(self.restaurant.restaurant_address, "abc")
        self.assertEqual(self.restaurant.restaurant_history, "good")

        # route
        self.assertEqual(self.route.route_name, "C-M-L")
        self.assertEqual(self.route.route_detail, "abc")

        # zoo
        self.assertEqual(self.zoo.attraction_website, "xyz")
        self.assertEqual(self.zoo.attraction_tel, "12345")
        self.assertEqual(self.zoo.attraction_introduction, "intro")

    # test relationship
    def test_relationship(self):
        expected_hotels = [self.hotel]
        actual_hotels = list(self.bar.hotel.all())  # many-to-many relationship
        self.assertQuerysetEqual(actual_hotels, expected_hotels, transform=lambda x: x)

        expected_hotels = [self.hotel]
        actual_hotels = list(self.museum.hotel.all())
        self.assertQuerysetEqual(actual_hotels, expected_hotels, transform=lambda x: x)

        expected_restaurants = [self.restaurant]
        actual_restaurants = list(self.cuisine.restaurant.all())
        self.assertQuerysetEqual(expected_restaurants, actual_restaurants, transform=lambda x: x)

        expected_route = [self.route]
        actual_route = list(self.city.route.all())
        self.assertQuerysetEqual(expected_route, actual_route, transform=lambda x: x)

        expected_city = self.city
        actual_city = self.hotel.city  # one-to-many relationship
        self.assertEqual(expected_city, actual_city)

    # test urls.py
    def test_url_exists1(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)  # redirect

    def test_url_exists2(self):
        response = self.client.get("/admin")
        self.assertEqual(response.status_code, 301)

    def test_url_exists3(self):
        response = self.client.get("/city/")
        self.assertEqual(response.status_code, 302)

    def test_url_exists4(self):
        response = self.client.get("/city/1/bar/")
        self.assertEqual(response.status_code, 302)


# test views.py, templates, authentication
class RestaurantDetailViewTestCase(TestCase):
    def setUp(self):
        # Create a user with the view_restaurant permission
        permission = Permission.objects.get(codename='view_restaurant')  # testing for authorization
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user.user_permissions.add(permission)
        self.user.save()

        # Create a restaurant to test with
        self.restaurant = Restaurant.objects.create(
            restaurant_name='KFC',
            restaurant_address='123 Main St',
            restaurant_history='A brief history of KFC',
        )

    def test_restaurant_detailview(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('sichuaninfo_restaurant_detail_urlpattern', args=[self.restaurant.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # testing for urls
        self.assertContains(response, self.restaurant.restaurant_name)  # testing for templates


class HotelDetailViewTestCase(TestCase):
    def setUp(self):
        # Create a user with the change_hotel permission
        permission = Permission.objects.get(codename='change_hotel')  # testing for authorization
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user.user_permissions.add(permission)
        self.user.save()

        # Create a restaurant to test with
        self.hotel = Hotel.objects.create(
            hotel_tel='123',
            hotel_website='http',
            hotel_name='good',
        )

    def test_hotel_detailview(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('sichuaninfo_hotel_detail_urlpattern', args=[self.hotel.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # testing for urls
        self.assertNotContains(response, self.hotel.hotel_tel)  # testing for templates


class TestAddRestaurant(TestCase):
    def setUp(self):
        # Create a user with the add_restaurant permission
        permission = Permission.objects.get(codename='add_restaurant')  # testing for authorization
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user.user_permissions.add(permission)
        self.user.save()

        # Create a restaurant object for testing
        self.restaurant = Restaurant.objects.create(
            restaurant_name='Test Restaurant',
            restaurant_address='123 Test St.',
            restaurant_tel='123-456-7890',
        )

    def test_add_restaurant(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('sichuaninfo_restaurant_create_urlpattern')
        data = {
            'restaurant_name': 'Test Restaurant',
            'address': '123 Test St.',
            'phone_number': '123-456-7890',
        }
        response = self.client.post(url, data)
        restaurant = Restaurant.objects.last()
        print(restaurant)  # added into the list
        self.assertEqual(response.status_code, 200)  # testing for urls
        self.assertEqual(Restaurant.objects.count(), 1)  # testing for templates
        self.assertEqual(restaurant.restaurant_name, 'Test Restaurant')  # testing for templates




