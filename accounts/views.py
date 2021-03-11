from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    return HttpResponse('Products page')


def customers(request):
    return HttpResponse('Customers page')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home),
#     path('about/', contact),
# ]
