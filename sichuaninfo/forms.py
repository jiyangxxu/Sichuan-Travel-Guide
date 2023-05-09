from django import forms

from sichuaninfo.models import Bar, Hotel, LocalFav, Mall, Monument, Museum, Cuisine, Restaurant, Zoo, Route


# cities are not shown to anyone, instead of superuser accesses the admin
class BarForm(forms.ModelForm):
    class Meta:
        model = Bar
        fields = '__all__'

    def clean_attraction_address(self):
        return self.cleaned_data['attraction_address'].strip()

    def clean_attraction_name(self):
        return self.cleaned_data['attraction_name'].strip()

    def clean_attraction_introduction(self):
        return self.cleaned_data['attraction_introduction'].strip()

    def clean_attraction_website(self):
        if len(self.cleaned_data['attraction_website']) == 0:
            result = self.cleaned_data['attraction_website']
        else:
            result = self.cleaned_data['attraction_website'].strip()
        return result

    def clean_attraction_tel(self):
        if len(self.cleaned_data['attraction_tel']) == 0:
            result = self.cleaned_data['attraction_tel']
        else:
            result = self.cleaned_data['attraction_tel'].strip()
        return result

    def clean_attraction_cost(self):
        if len(self.cleaned_data['attraction_cost']) == 0:
            result = self.cleaned_data['attraction_cost']
        else:
            result = self.cleaned_data['attraction_cost'].strip()
        return result

    def clean_suggest_duration(self):
        if len(self.cleaned_data['suggest_duration']) == 0:
            result = self.cleaned_data['suggest_duration']
        else:
            result = self.cleaned_data['suggest_duration'].strip()
        return result


class LocalFavForm(forms.ModelForm):
    class Meta:
        model = LocalFav
        fields = '__all__'

    def clean_attraction_address(self):
        return self.cleaned_data['attraction_address'].strip()

    def clean_attraction_name(self):
        return self.cleaned_data['attraction_name'].strip()

    def clean_attraction_introduction(self):
        return self.cleaned_data['attraction_introduction'].strip()

    def clean_attraction_website(self):
        if len(self.cleaned_data['attraction_website']) == 0:
            result = self.cleaned_data['attraction_website']
        else:
            result = self.cleaned_data['attraction_website'].strip()
        return result

    def clean_attraction_tel(self):
        if len(self.cleaned_data['attraction_tel']) == 0:
            result = self.cleaned_data['attraction_tel']
        else:
            result = self.cleaned_data['attraction_tel'].strip()
        return result

    def clean_attraction_cost(self):
        if len(self.cleaned_data['attraction_cost']) == 0:
            result = self.cleaned_data['attraction_cost']
        else:
            result = self.cleaned_data['attraction_cost'].strip()
        return result


class MallForm(forms.ModelForm):
    class Meta:
        model = Mall
        fields = '__all__'

    def clean_attraction_address(self):
        return self.cleaned_data['attraction_address'].strip()

    def clean_attraction_name(self):
        return self.cleaned_data['attraction_name'].strip()

    def clean_attraction_introduction(self):
        return self.cleaned_data['attraction_introduction'].strip()

    def clean_attraction_website(self):
        if len(self.cleaned_data['attraction_website']) == 0:
            result = self.cleaned_data['attraction_website']
        else:
            result = self.cleaned_data['attraction_website'].strip()
        return result

    def clean_attraction_tel(self):
        if len(self.cleaned_data['attraction_tel']) == 0:
            result = self.cleaned_data['attraction_tel']
        else:
            result = self.cleaned_data['attraction_tel'].strip()
        return result

    def clean_attraction_cost(self):
        if len(self.cleaned_data['attraction_cost']) == 0:
            result = self.cleaned_data['attraction_cost']
        else:
            result = self.cleaned_data['attraction_cost'].strip()
        return result


class MonumentForm(forms.ModelForm):
    class Meta:
        model = Monument
        fields = '__all__'

    def clean_attraction_address(self):
        return self.cleaned_data['attraction_address'].strip()

    def clean_attraction_name(self):
        return self.cleaned_data['attraction_name'].strip()

    def clean_attraction_introduction(self):
        return self.cleaned_data['attraction_introduction'].strip()

    def clean_attraction_website(self):
        if len(self.cleaned_data['attraction_website']) == 0:
            result = self.cleaned_data['attraction_website']
        else:
            result = self.cleaned_data['attraction_website'].strip()
        return result

    def clean_attraction_tel(self):
        if len(self.cleaned_data['attraction_tel']) == 0:
            result = self.cleaned_data['attraction_tel']
        else:
            result = self.cleaned_data['attraction_tel'].strip()
        return result

    def clean_attraction_cost(self):
        if len(self.cleaned_data['attraction_cost']) == 0:
            result = self.cleaned_data['attraction_cost']
        else:
            result = self.cleaned_data['attraction_cost'].strip()
        return result


class MuseumForm(forms.ModelForm):
    class Meta:
        model = Museum
        fields = '__all__'

    def clean_attraction_address(self):
        return self.cleaned_data['attraction_address'].strip()

    def clean_attraction_name(self):
        return self.cleaned_data['attraction_name'].strip()

    def clean_attraction_introduction(self):
        return self.cleaned_data['attraction_introduction'].strip()

    def clean_attraction_website(self):
        if len(self.cleaned_data['attraction_website']) == 0:
            result = self.cleaned_data['attraction_website']
        else:
            result = self.cleaned_data['attraction_website'].strip()
        return result

    def clean_attraction_tel(self):
        if len(self.cleaned_data['attraction_tel']) == 0:
            result = self.cleaned_data['attraction_tel']
        else:
            result = self.cleaned_data['attraction_tel'].strip()
        return result

    def clean_attraction_cost(self):
        if len(self.cleaned_data['attraction_cost']) == 0:
            result = self.cleaned_data['attraction_cost']
        else:
            result = self.cleaned_data['attraction_cost'].strip()
        return result


class ZooForm(forms.ModelForm):
    class Meta:
        model = Zoo
        fields = '__all__'

    def clean_attraction_address(self):
        return self.cleaned_data['attraction_address'].strip()

    def clean_attraction_name(self):
        return self.cleaned_data['attraction_name'].strip()

    def clean_attraction_introduction(self):
        return self.cleaned_data['attraction_introduction'].strip()

    def clean_attraction_website(self):
        if len(self.cleaned_data['attraction_website']) == 0:
            result = self.cleaned_data['attraction_website']
        else:
            result = self.cleaned_data['attraction_website'].strip()
        return result

    def clean_attraction_tel(self):
        if len(self.cleaned_data['attraction_tel']) == 0:
            result = self.cleaned_data['attraction_tel']
        else:
            result = self.cleaned_data['attraction_tel'].strip()
        return result

    def clean_attraction_cost(self):
        if len(self.cleaned_data['attraction_cost']) == 0:
            result = self.cleaned_data['attraction_cost']
        else:
            result = self.cleaned_data['attraction_cost'].strip()
        return result


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

    def clean_hotel_name(self):
        return self.cleaned_data['hotel_name'].strip()

    def clean_hotel_address(self):
        return self.cleaned_data['hotel_address'].strip()

    def clean_introduction(self):
        return self.cleaned_data['introduction'].strip()

    def clean_hotel_tel(self):
        if len(self.cleaned_data['hotel_tel']) == 0:
            result = self.cleaned_data['hotel_tel']
        else:
            result = self.cleaned_data['hotel_tel'].strip()
        return result

    def clean_hotel_website(self):
        if len(self.cleaned_data['hotel_website']) == 0:
            result = self.cleaned_data['hotel_website']
        else:
            result = self.cleaned_data['hotel_website'].strip()
        return result

    def clean_hotel_cost_per_night(self):
        if len(self.cleaned_data['hotel_cost_per_night']) == 0:
            result = self.cleaned_data['hotel_cost_per_night']
        else:
            result = self.cleaned_data['hotel_cost_per_night'].strip()
        return result


class CuisineForm(forms.ModelForm):
    class Meta:
        model = Cuisine
        fields = '__all__'

    def clean_cuisine_name(self):
        return self.cleaned_data['cuisine_name'].strip()

    def clean_course_history(self):
        return self.cleaned_data['course_history'].strip()


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

    def clean_restaurant_name(self):
        return self.cleaned_data['restaurant_name'].strip()

    def clean_restaurant_address(self):
        return self.cleaned_data['restaurant_address'].strip()

    def clean_restaurant_history(self):
        return self.cleaned_data['restaurant_history'].strip()

    def clean_cost(self):
        if len(self.cleaned_data['cost']) == 0:
            result = self.cleaned_data['cost']
        else:
            result = self.cleaned_data['cost'].strip()
        return result

    def clean_restaurant_tel(self):
        if len(self.cleaned_data['restaurant_tel']) == 0:
            result = self.cleaned_data['restaurant_tel']
        else:
            result = self.cleaned_data['restaurant_tel'].strip()
        return result


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'

    def clean_route_name(self):
        return self.cleaned_data['route_name'].strip()

    def clean_route_detail(self):
        return self.cleaned_data['route_detail'].strip()
