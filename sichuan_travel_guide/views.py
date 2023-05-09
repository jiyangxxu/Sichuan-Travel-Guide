from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('sichuaninfo_city_list_urlpattern')