from django.urls import path, reverse_lazy

from sichuaninfo.views import BarList, HotelList, LocalFavList, MallList, MonumentList, MuseumList, RestaurantList, \
    ZooList, RouteList, CityList, \
    CityDetail, BarDetail, HotelDetail, LocalFavDetail, MallDetail, MonumentDetail, MuseumDetail, RestaurantDetail, \
    ZooDetail, RouteDetail, attraction_list, CuisineDetail, BarCreate, HotelCreate, LocalFavCreate, MallCreate, \
    MonumentCreate, MuseumCreate, ZooCreate, CuisineCreate, RestaurantCreate, RouteCreate, BarUpdate, BarDelete, \
    HotelUpdate, HotelDelete, LocalFavUpdate, LocalFavDelete, MallUpdate, MallDelete, MonumentUpdate, MonumentDelete, \
    MuseumUpdate, MuseumDelete, ZooUpdate, ZooDelete, CuisineUpdate, CuisineDelete, RestaurantDelete, RestaurantUpdate, \
    RouteUpdate, RouteDelete, CuisineList

urlpatterns = [
    path('city/<int:pk>/attraction/',
         attraction_list,
         name='sichuaninfo_attraction_list_urlpattern'),

    path('city/<int:pk>/bar/', BarList.as_view(),
         name='sichuaninfo_bar_list_urlpattern'),

    path('bar/<int:pk>/', BarDetail.as_view(),
         name='sichuaninfo_bar_detail_urlpattern'),

    path('bar/create/', BarCreate.as_view(),
         name='sichuaninfo_bar_create_urlpattern'),

    path('bar/<int:pk>/update/',
         BarUpdate.as_view(),
         name='sichuaninfo_bar_update_urlpattern'),

    path('bar/<int:pk>/delete/',
         BarDelete.as_view(success_url=reverse_lazy('sichuaninfo_bar_list_urlpattern')), name='sichuaninfo_bar_delete_urlpattern'),

    path('city/',
         CityList.as_view(),
         name='sichuaninfo_city_list_urlpattern'),

    path('city/<int:pk>/',
         CityDetail.as_view(),
         name='sichuaninfo_city_detail_urlpattern'),

    path('city/<int:pk>/hotel/', HotelList.as_view(),
         name='sichuaninfo_hotel_list_urlpattern'),

    path('hotel/<int:pk>/',
         HotelDetail.as_view(),
         name='sichuaninfo_hotel_detail_urlpattern'),

    path('hotel/create/', HotelCreate.as_view(),
         name='sichuaninfo_hotel_create_urlpattern'),

    path('hotel/<int:pk>/update/',
         HotelUpdate.as_view(),
         name='sichuaninfo_hotel_update_urlpattern'),

    path('hotel/<int:pk>/delete/',
         HotelDelete.as_view(),
         name='sichuaninfo_hotel_delete_urlpattern'),

    path('city/<int:pk>/localfav/', LocalFavList.as_view(),
         name='sichuaninfo_localfav_list_urlpattern'),

    path('localfav/<int:pk>/',
         LocalFavDetail.as_view(),
         name='sichuaninfo_localfav_detail_urlpattern'),

    path('localfav/create/', LocalFavCreate.as_view(),
         name='sichuaninfo_localfav_create_urlpattern'),

    path('localfav/<int:pk>/update/',
         LocalFavUpdate.as_view(),
         name='sichuaninfo_localfav_update_urlpattern'),

    path('localfav/<int:pk>/delete/',
         LocalFavDelete.as_view(),
         name='sichuaninfo_localfav_delete_urlpattern'),

    path('city/<int:pk>/mall/', MallList.as_view(),
         name='sichuaninfo_mall_list_urlpattern'),

    path('mall/<int:pk>/',
         MallDetail.as_view(),
         name='sichuaninfo_mall_detail_urlpattern'),

    path('mall/create/', MallCreate.as_view(),
         name='sichuaninfo_mall_create_urlpattern'),

    path('mall/<int:pk>/update/',
         MallUpdate.as_view(),
         name='sichuaninfo_mall_update_urlpattern'),

    path('mall/<int:pk>/delete/',
         MallDelete.as_view(),
         name='sichuaninfo_mall_delete_urlpattern'),

    path('city/<int:pk>/monument/', MonumentList.as_view(),
         name='sichuaninfo_monument_list_urlpattern'),

    path('monument/<int:pk>/',
         MonumentDetail.as_view(),
         name='sichuaninfo_monument_detail_urlpattern'),

    path('monument/create/', MonumentCreate.as_view(),
         name='sichuaninfo_monument_create_urlpattern'),

    path('monument/<int:pk>/update/',
         MonumentUpdate.as_view(),
         name='sichuaninfo_monument_update_urlpattern'),

    path('monument/<int:pk>/delete/',
         MonumentDelete.as_view(),
         name='sichuaninfo_monument_delete_urlpattern'),

    path('city/<int:pk>/museum/', MuseumList.as_view(),
         name='sichuaninfo_museum_list_urlpattern'),

    path('museum/<int:pk>/',
         MuseumDetail.as_view(),
         name='sichuaninfo_museum_detail_urlpattern'),

    path('museum/create/', MuseumCreate.as_view(),
         name='sichuaninfo_museum_create_urlpattern'),

    path('museum/<int:pk>/update/',
         MuseumUpdate.as_view(),
         name='sichuaninfo_museum_update_urlpattern'),

    path('museum/<int:pk>/delete/',
         MuseumDelete.as_view(),
         name='sichuaninfo_museum_delete_urlpattern'),

    path('city/<int:pk>/zoo/', ZooList.as_view(),
         name='sichuaninfo_zoo_list_urlpattern'),

    path('zoo/<int:pk>/',
         ZooDetail.as_view(),
         name='sichuaninfo_zoo_detail_urlpattern'),

    path('zoo/create/', ZooCreate.as_view(),
         name='sichuaninfo_zoo_create_urlpattern'),

    path('zoo/<int:pk>/update/',
         ZooUpdate.as_view(),
         name='sichuaninfo_zoo_update_urlpattern'),

    path('zoo/<int:pk>/delete/',
         ZooDelete.as_view(),
         name='sichuaninfo_zoo_delete_urlpattern'),

    path('city/<int:pk>/cuisine/',
         CuisineList.as_view(),
         name='sichuaninfo_cuisine_list_urlpattern'),

    path('cuisine/<int:pk>/',
         CuisineDetail.as_view(),
         name='sichuaninfo_cuisine_detail_urlpattern'),

    path('cuisine/create/', CuisineCreate.as_view(),
         name='sichuaninfo_cuisine_create_urlpattern'),

    path('cuisine/<int:pk>/update/',
         CuisineUpdate.as_view(),
         name='sichuaninfo_cuisine_update_urlpattern'),

    path('bar/<int:pk>/delete/',
         CuisineDelete.as_view(),
         name='sichuaninfo_cuisine_delete_urlpattern'),

    path('city/<int:pk>/restaurant/', RestaurantList.as_view(),
         name='sichuaninfo_restaurant_list_urlpattern'),

    path('restaurant/<int:pk>/',
         RestaurantDetail.as_view(),
         name='sichuaninfo_restaurant_detail_urlpattern'),

    path('restaurant/create/', RestaurantCreate.as_view(),
         name='sichuaninfo_restaurant_create_urlpattern'),

    path('restaurant/<int:pk>/update/',
         RestaurantUpdate.as_view(),
         name='sichuaninfo_restaurant_update_urlpattern'),

    path('restaurant/<int:pk>/delete/',
         RestaurantDelete.as_view(),
         name='sichuaninfo_restaurant_delete_urlpattern'),


    path('city/<int:pk>/route/',
         RouteList.as_view(),
         name='sichuaninfo_route_list_urlpattern'),

    path('route/<int:pk>/',
         RouteDetail.as_view(),
         name='sichuaninfo_route_detail_urlpattern'),

    path('route/create/', RouteCreate.as_view(),
         name='sichuaninfo_route_create_urlpattern'),

    path('route/<int:pk>/update/',
         RouteUpdate.as_view(),
         name='sichuaninfo_route_update_urlpattern'),

    path('route/<int:pk>/delete/',
         RouteDelete.as_view(),
         name='sichuaninfo_route_delete_urlpattern'),

    ]