from django.db import models
from django.urls import reverse


class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=45)
    route_detail = models.CharField(max_length=450)

    def __str__(self):
        return self.route_name

    def get_absolute_url(self):
        return reverse('sichuaninfo_route_detail_urlpattern',  # add later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_route_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_route_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['route_name']


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=45, unique=True)
    city_intro = models.CharField(max_length=1500, unique=True)

    route = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return '%s' % self.city_name

    def get_absolute_url(self):
        return reverse('sichuaninfo_city_detail_urlpattern',  # added later
                       kwargs={'pk': self.pk}
                       )


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=50, unique=True)
    hotel_address = models.CharField(max_length=100, unique=True)
    hotel_tel = models.CharField(max_length=50, unique=False, default='')
    hotel_website = models.CharField(blank=True, max_length=200, unique=False, default='')
    hotel_cost_per_night = models.CharField(max_length=50, unique=False, default='')
    introduction = models.CharField(max_length=600, unique=True)

    city = models.ForeignKey(City, related_name='hotels', on_delete=models.PROTECT, null=True)
    route = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return self.hotel_name

    def get_absolute_url(self):
        return reverse('sichuaninfo_hotel_detail_urlpattern',  # added later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_hotel_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_hotel_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['hotel_name']


class Zoo(models.Model):
    zoo_id = models.AutoField(primary_key=True)
    attraction_address = models.CharField(max_length=100, unique=True)
    attraction_name = models.CharField(max_length=50, unique=True)
    attraction_website = models.CharField(max_length=200, unique=False, blank=True, default='')
    attraction_introduction = models.CharField(max_length=600, unique=True)
    attraction_tel = models.CharField(blank=True, max_length=50, unique=False, default='')
    attraction_cost = models.CharField(blank=True, max_length=50, unique=False, default='')

    # foreign keys
    hotel = models.ManyToManyField(Hotel, blank=True)
    city = models.ForeignKey(City, related_name='zoos', on_delete=models.PROTECT, null=True)
    route = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return '%s' % self.attraction_name

    class Meta:
        ordering = ['attraction_name']

    def get_absolute_url(self):
        return reverse('sichuaninfo_zoo_detail_urlpattern',  # added later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_zoo_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_zoo_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class Museum(models.Model):
    museum_id = models.AutoField(primary_key=True)
    attraction_address = models.CharField(max_length=100, unique=True)
    attraction_name = models.CharField(max_length=50, unique=True)
    attraction_website = models.CharField(max_length=200, unique=False, blank=True, default='')
    attraction_introduction = models.CharField(max_length=600, unique=True)
    attraction_tel = models.CharField(blank=True, max_length=50, unique=False, default='')
    attraction_cost = models.CharField(blank=True, max_length=50, unique=False, default='')

    # foreign keys
    hotel = models.ManyToManyField(Hotel, blank=True)
    city = models.ForeignKey(City, related_name='museums', on_delete=models.PROTECT, null=True)
    route = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return '%s' % self.attraction_name

    class Meta:
        ordering = ['attraction_name']

    def get_absolute_url(self):
        return reverse('sichuaninfo_museum_detail_urlpattern',  # added later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_museum_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_museum_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class Monument(models.Model):
    monument_id = models.AutoField(primary_key=True)
    attraction_address = models.CharField(max_length=100, unique=True)
    attraction_name = models.CharField(max_length=50, unique=True)
    attraction_website = models.CharField(max_length=200, unique=False, blank=True, default='')
    attraction_introduction = models.CharField(max_length=600, unique=True)
    attraction_tel = models.CharField(blank=True, max_length=50, unique=False, default='')
    attraction_cost = models.CharField(blank=True, max_length=50, unique=False, default='')
    # foreign keys
    hotel = models.ManyToManyField(Hotel, blank=True)
    city = models.ForeignKey(City, related_name='monuments', on_delete=models.PROTECT, null=True)
    route = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return '%s' % self.attraction_name

    class Meta:
        ordering = ['attraction_name']

    def get_absolute_url(self):
        return reverse('sichuaninfo_monument_detail_urlpattern',  # added later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_monument_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_monument_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class LocalFav(models.Model):
    localfav_id = models.AutoField(primary_key=True)
    attraction_address = models.CharField(max_length=100, unique=True)
    attraction_name = models.CharField(max_length=50, unique=True)
    attraction_website = models.CharField(max_length=200, unique=False, blank=True, default='')
    attraction_introduction = models.CharField(max_length=600, unique=True)
    attraction_tel = models.CharField(blank=True, max_length=50, unique=False, default='')
    attraction_cost = models.CharField(blank=True, max_length=50, unique=False, default='')

    # foreign keys
    hotel = models.ManyToManyField(Hotel, blank=True)
    city = models.ForeignKey(City, related_name='localfavs', on_delete=models.PROTECT, null=True)
    route = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return '%s' % self.attraction_name

    class Meta:
        ordering = ['attraction_name']

    def get_absolute_url(self):
        return reverse('sichuaninfo_localfav_detail_urlpattern',  # added later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_localfav_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_localfav_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class Mall(models.Model):
    mall_id = models.AutoField(primary_key=True)
    attraction_address = models.CharField(max_length=100, unique=True)
    attraction_name = models.CharField(max_length=50, unique=True)
    attraction_website = models.CharField(max_length=200, unique=False, blank=True, default='')
    attraction_introduction = models.CharField(max_length=600, unique=True)
    attraction_tel = models.CharField(blank=True, max_length=50, unique=False, default='')
    attraction_cost = models.CharField(blank=True, max_length=50, unique=False, default='')

    # foreign keys
    hotel = models.ManyToManyField(Hotel, blank=True)
    city = models.ForeignKey(City, related_name='malls', on_delete=models.PROTECT, null=True)
    route = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return '%s' % self.attraction_name

    class Meta:
        ordering = ['attraction_name']

    def get_absolute_url(self):
        return reverse('sichuaninfo_mall_detail_urlpattern',  # added later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_mall_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_mall_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class Bar(models.Model):
    bar_id = models.AutoField(primary_key=True)
    attraction_address = models.CharField(max_length=100)
    attraction_name = models.CharField(max_length=50)
    attraction_website = models.CharField(max_length=200, blank=True, default='')
    attraction_introduction = models.CharField(max_length=600)
    attraction_tel = models.CharField(blank=True, max_length=30, default='')
    attraction_cost = models.CharField(blank=True, max_length=50, unique=False, default='')

    suggest_duration = models.CharField(max_length=20, blank=True, default='')

    # foreign keys
    hotel = models.ManyToManyField(Hotel, blank=True)
    city = models.ForeignKey(City, related_name='bars', on_delete=models.PROTECT, null=True)
    route = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return '%s' % self.attraction_name

    class Meta:
        ordering = ['attraction_name']

    def get_absolute_url(self):
        return reverse('sichuaninfo_bar_detail_urlpattern',  # added later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_bar_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_bar_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=45)
    restaurant_address = models.CharField(max_length=100)
    restaurant_tel = models.CharField(blank=True, unique=False, default='', max_length=100)
    restaurant_history = models.CharField(max_length=600)
    cost = models.CharField(blank=True, max_length=50, unique=False, default='')

    # foreign keys
    hotel = models.ManyToManyField(Hotel, blank=True)
    city = models.ForeignKey(City, related_name='restaurants', on_delete=models.PROTECT, null=True)
    route = models.ManyToManyField(Route, blank=True)

    def __str__(self):
        return self.restaurant_name

    def get_absolute_url(self):
        return reverse('sichuaninfo_restaurant_detail_urlpattern',  # add later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_restaurant_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_restaurant_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['restaurant_name']


class Cuisine(models.Model):
    cuisine_id = models.AutoField(primary_key=True)
    cuisine_name = models.CharField(max_length=20)
    cuisine_history = models.CharField(max_length=600)

    def __str__(self):
        return self.cuisine_name

    def get_absolute_url(self):
        return reverse('sichuaninfo_cuisine_detail_urlpattern',  # add later
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('sichuaninfo_cuisine_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sichuaninfo_cuisine_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    # foreign keys
    restaurant = models.ManyToManyField(Restaurant, blank=True)
    city = models.ForeignKey(City, related_name='cuisine', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['cuisine_name']



