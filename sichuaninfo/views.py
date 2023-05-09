from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sichuaninfo.utils import ObjectCreateMixin, PageLinksMixin

from sichuaninfo.models import City, Bar, Hotel, LocalFav, Mall, Monument, Museum, Cuisine, Restaurant, Zoo, \
    Route


from django.views import View
from django.shortcuts import render

from .forms import BarForm, HotelForm, LocalFavForm, MallForm, MonumentForm, MuseumForm, ZooForm, CuisineForm, \
    RestaurantForm, RouteForm
from .models import City
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render


def check_view_city_permission(user):
    return user.has_perm('sichuaninfo.view_city')


def attraction_list(request, pk):
    city = get_object_or_404(City, pk=pk)
    context = {
        'city': city,
        'city_slug': city.pk,
    }
    city_list = City.objects.all()
    if not check_view_city_permission(request.user):
        return user_test_failure(request)
    return render(request, 'sichuaninfo/attraction_list.html', {'city_list': city_list, 'context': context})


def user_test_failure(request, *args, **kwargs):
    raise PermissionDenied("You don't have permission to access this page.")


class CityList(LoginRequiredMixin, View, PermissionRequiredMixin):
    def get(self, request):
        city_list = City.objects.all()
        return render(request, 'sichuaninfo/city_list.html', {'city_list': city_list})

    permission_required = 'sichuaninfo.view_city'


class BarList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = Bar
    template_name = 'sichuaninfo/bar_list.html'
    context_object_name = 'bar_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_bar'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        bar_list = self.get_queryset()
        return render(request, 'sichuaninfo/bar_list.html',
                      {'city_list': city_list, 'bar_list': bar_list})


class BarDetail(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_bar'

    def get(self, request, pk):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        bar = get_object_or_404(
            Bar,
            pk=pk
        )
        city_list = City.objects.all()
        return render(
            request,
            'sichuaninfo/bar_detail.html',
            {'bar': bar, 'city_list': city_list}
        )


class BarCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = BarForm
    model = Bar
    template_name = 'sichuaninfo/bar_form.html'
    permission_required = 'sichuaninfo.add_bar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class BarUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = BarForm
    model = Bar
    template_name = 'sichuaninfo/bar_form_update.html'
    permission_required = 'sichuaninfo.change_bar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class BarDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Bar
    permission_required = 'sichuaninfo.delete_bar'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_bar_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class LocalFavDetail(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_localfav'

    def get(self, request, pk):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        localfav = get_object_or_404(
            LocalFav,
            pk=pk
        )
        city_list = City.objects.all()
        return render(
            request,
            'sichuaninfo/localfav_detail.html',
            {'localfav': localfav, 'city_list': city_list}
        )


class LocalFavList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = LocalFav
    template_name = 'sichuaninfo/localfav_list.html'
    context_object_name = 'localfav_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_localfav'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        localfav_list = self.get_queryset()
        return render(request, 'sichuaninfo/localfav_list.html',
                      {'city_list': city_list, 'localfav_list': localfav_list})


class LocalFavCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = LocalFavForm
    model = LocalFav
    template_name = 'sichuaninfo/localfav_form.html'
    permission_required = 'sichuaninfo.add_localfav'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class LocalFavUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = LocalFavForm
    model = LocalFav
    template_name = 'sichuaninfo/localfav_form_update.html'
    permission_required = 'sichuaninfo.change_localfav'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class LocalFavDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = LocalFav
    permission_required = 'sichuaninfo.delete_localfav'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_localfav_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class MallList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = Mall
    template_name = 'sichuaninfo/mall_list.html'
    context_object_name = 'mall_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_mall'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        mall_list = self.get_queryset()
        return render(request, 'sichuaninfo/mall_list.html',
                      {'city_list': city_list, 'mall_list': mall_list})


class MallDetail(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_mall'

    def get(self, request, pk):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        mall = get_object_or_404(
            Mall,
            pk=pk
        )
        city_list = City.objects.all()
        return render(
            request,
            'sichuaninfo/mall_detail.html',
            {'mall': mall, 'city_list': city_list}
        )


class MallCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = MallForm
    model = Mall
    template_name = 'sichuaninfo/mall_form.html'
    permission_required = 'sichuaninfo.add_mall'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class MallUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = MallForm
    model = Mall
    template_name = 'sichuaninfo/mall_form_update.html'
    permission_required = 'sichuaninfo.change_mall'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class MallDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Mall
    permission_required = 'sichuaninfo.delete_mall'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_mall_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class MonumentList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = Monument
    template_name = 'sichuaninfo/monument_list.html'
    context_object_name = 'monument_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_monument'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        monument_list = self.get_queryset()
        return render(request, 'sichuaninfo/monument_list.html',
                      {'city_list': city_list, 'monument_list': monument_list})


class MonumentDetail(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_monument'

    def get(self, request, pk):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        monument = get_object_or_404(
            Monument,
            pk=pk
        )
        city_list = City.objects.all()
        return render(
            request,
            'sichuaninfo/monument_detail.html',
            {'monument': monument, 'city_list': city_list}
        )


class MonumentCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.add_monument'

    form_class = MonumentForm
    model = Monument
    template_name = 'sichuaninfo/monument_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class MonumentUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.change_monument'

    form_class = MonumentForm
    model = Monument
    template_name = 'sichuaninfo/monument_form_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class MonumentDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Monument
    permission_required = 'sichuaninfo.delete_monument'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_monument_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class ZooList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = Zoo
    template_name = 'sichuaninfo/zoo_list.html'
    context_object_name = 'zoo_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_zoo'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        zoo_list = self.get_queryset()
        return render(request, 'sichuaninfo/zoo_list.html',
                      {'city_list': city_list, 'zoo_list': zoo_list})


class ZooDetail(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_zoo'

    def get(self, request, pk):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        zoo = get_object_or_404(
            Zoo,
            pk=pk
        )
        city_list = City.objects.all()
        return render(
            request,
            'sichuaninfo/zoo_detail.html',
            {'zoo': zoo, 'city_list': city_list}
        )


class ZooCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = ZooForm
    model = Zoo
    template_name = 'sichuaninfo/zoo_form.html'
    permission_required = 'sichuaninfo.add_zoo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class ZooUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = ZooForm
    model = Zoo
    template_name = 'sichuaninfo/zoo_form_update.html'
    permission_required = 'sichuaninfo.change_zoo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class ZooDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Zoo
    permission_required = 'sichuaninfo.delete_zoo'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_zoo_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class MuseumList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = Museum
    template_name = 'sichuaninfo/museum_list.html'
    context_object_name = 'museum_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_museum'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        museum_list = self.get_queryset()
        return render(request, 'sichuaninfo/museum_list.html',
                      {'city_list': city_list, 'museum_list': museum_list})


class MuseumDetail(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_museum'

    def get(self, request, pk):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        museum = get_object_or_404(
            Museum,
            pk=pk
        )
        city_list = City.objects.all()
        return render(
            request,
            'sichuaninfo/museum_detail.html',
            {'museum': museum, 'city_list': city_list}
        )


class MuseumCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = MuseumForm
    model = Museum
    template_name = 'sichuaninfo/museum_form.html'
    permission_required = 'sichuaninfo.add_museum'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class MuseumUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = MuseumForm
    model = Museum
    template_name = 'sichuaninfo/museum_form_update.html'
    permission_required = 'sichuaninfo.change_museum'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class MuseumDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Museum
    permission_required = 'sichuaninfo.delete_museum'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_museum_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class CuisineList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = Cuisine
    template_name = 'sichuaninfo/cuisine_list.html'
    context_object_name = 'cuisine_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_cuisine'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        cuisine_list = self.get_queryset()
        return render(request, 'sichuaninfo/cuisine_list.html',
                      {'city_list': city_list, 'cuisine_list': cuisine_list})


class CuisineDetail(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_cuisine'

    def get(self, request, pk):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        cuisine = get_object_or_404(
            Cuisine,
            pk=pk
        )
        city_list = City.objects.all()
        restaurant_list = cuisine.restaurant.all()
        return render(
            request,
            'sichuaninfo/cuisine_detail.html',
            {'cuisine': cuisine, 'city_list': city_list, 'restaurant': restaurant_list}
        )


class CuisineCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = CuisineForm
    model = Cuisine
    template_name = 'sichuaninfo/cuisine_form.html'
    permission_required = 'sichuaninfo.add_cuisine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class CuisineUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = CuisineForm
    model = Cuisine
    template_name = 'sichuaninfo/cuisine_form_update.html'
    permission_required = 'sichuaninfo.change_cuisine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class CuisineDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Cuisine
    permission_required = 'sichuaninfo.delete_cuisine'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_cuisine_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class RestaurantList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = Restaurant
    template_name = 'sichuaninfo/restaurant_list.html'
    context_object_name = 'restaurant_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_restaurant'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        restaurant_list = self.get_queryset()
        return render(request, 'sichuaninfo/restaurant_list.html',
                      {'city_list': city_list, 'restaurant_list': restaurant_list})


class RestaurantDetail(LoginRequiredMixin, View, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_restaurant'

    def get(self, request, pk):
        restaurant = get_object_or_404(
            Restaurant,
            pk=pk
        )
        cuisine_list = list(restaurant.cuisine_set.all())
        city_list = City.objects.all()
        return render(
            request,
            'sichuaninfo/restaurant_detail.html',
            {'restaurant': restaurant,
             'cuisine_list': cuisine_list,
             'city_list': city_list}
        )


class RestaurantCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = RestaurantForm
    model = Restaurant
    template_name = 'sichuaninfo/restaurant_form.html'
    permission_required = 'sichuaninfo.add_restaurant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class RestaurantUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = RestaurantForm
    model = Restaurant
    template_name = 'sichuaninfo/restaurant_form_update.html'
    permission_required = 'sichuaninfo.change_restaurant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class RestaurantDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Restaurant
    permission_required = 'sichuaninfo.delete_restaurant'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_restaurant_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class HotelList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = Hotel
    template_name = 'sichuaninfo/hotel_list.html'
    context_object_name = 'hotel_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_hotel'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        hotel_list = self.get_queryset()
        return render(request, 'sichuaninfo/hotel_list.html',
                      {'city_list': city_list, 'hotel_list': hotel_list})


class HotelDetail(LoginRequiredMixin, View, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_hotel'

    def get(self, request, pk):
        hotel = get_object_or_404(
            Hotel,
            pk=pk
        )
        hotel = hotel
        zoo_list = list(hotel.zoo_set.all())
        bar_list = list(hotel.bar_set.all())
        localfav_list = list(hotel.localfav_set.all())
        mall_list = list(hotel.mall_set.all())
        monument_list = list(hotel.monument_set.all())
        museum_list = list(hotel.museum_set.all())
        restaurant_list = list(hotel.restaurant_set.all())
        city_list = City.objects.all()
        return render(
            request,
            'sichuaninfo/hotel_detail.html',
            {'hotel': hotel,
             'zoo': zoo_list,
             'bar': bar_list,
             'localfav': localfav_list,
             'mall': mall_list,
             'monument': monument_list,
             'museum': museum_list,
             'restaurant': restaurant_list,
             'city_list': city_list}
        )


class HotelCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = HotelForm
    model = Hotel
    template_name = 'sichuaninfo/hotel_form.html'
    permission_required = 'sichuaninfo.add_hotel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class HotelUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = HotelForm
    model = Hotel
    template_name = 'sichuaninfo/hotel_form_update.html'
    permission_required = 'sichuaninfo.change_hotel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class HotelDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Hotel
    permission_required = 'sichuaninfo.delete_hotel'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_hotel_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class CityDetail(LoginRequiredMixin, DetailView, PermissionRequiredMixin):
    model = City
    template_name = 'sichuaninfo/city_detail.html'
    context_object_name = 'city'
    permission_required = 'sichuaninfo.view_city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_pk'] = self.object.pk
        context['route'] = self.model.route
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)


class RouteList(LoginRequiredMixin, ListView, PageLinksMixin, PermissionRequiredMixin):
    model = Route
    template_name = 'sichuaninfo/route_list.html'
    context_object_name = 'route_list'
    paginate_by = 10
    permission_required = 'sichuaninfo.view_route'

    def get_queryset(self):
        city_pk = self.kwargs.get('pk')

        # Filter the bars based on the city
        city = get_object_or_404(City, pk=city_pk)
        queryset = super().get_queryset().filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_pk = self.kwargs.get('pk')
        city = get_object_or_404(City, pk=city_pk)
        if city:
            context['city_pk'] = city.pk
            context['city'] = city
        context['city_list'] = City.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("You don't have permission to access this page.")
        city_list = City.objects.all()
        route_list = self.get_queryset()
        return render(request, 'sichuaninfo/route_list.html',
                      {'city_list': city_list, 'route_list': route_list})


class RouteDetail(LoginRequiredMixin, View, PermissionRequiredMixin):
    permission_required = 'sichuaninfo.view_route'

    def get(self, request, pk):
        route = get_object_or_404(
            Route,
            pk=pk
        )

        city = list(route.city_set.all())
        city_list=City.objects.all()
        hotel_list = list(route.hotel_set.all())
        zoos_list = list(route.zoo_set.all())
        bars_list = list(route.bar_set.all())
        localfav_list = list(route.localfav_set.all())
        mall_list = list(route.mall_set.all())
        monument_list = list(route.monument_set.all())
        museum_list = list(route.museum_set.all())
        restaurant_list = list(route.restaurant_set.all())
        return render(
            request,
            'sichuaninfo/route_detail.html',
            {'route': route,
             'hotel': hotel_list,
             'zoo': zoos_list,
             'bar': bars_list,
             'localfav': localfav_list,
             'mall': mall_list,
             'monument': monument_list,
             'museum': museum_list,
             'restaurant': restaurant_list,
             'city_list': city_list,   # all the cities
             'city': city}  # the contained cities
        )


class RouteCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = RouteForm
    model = Route
    template_name = 'sichuaninfo/route_form.html'
    permission_required = 'sichuaninfo.add_route'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class RouteUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = RouteForm
    model = Route
    template_name = 'sichuaninfo/route_form_update.html'
    permission_required = 'sichuaninfo.change_route'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context


class RouteDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Route
    permission_required = 'sichuaninfo.delete_route'

    def get_success_url(self):
        city_pk = self.get_object().city.pk
        return reverse_lazy('sichuaninfo_route_list_urlpattern', args=[city_pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context
