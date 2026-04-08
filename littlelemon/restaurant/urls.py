#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken



urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('booking/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'})),


]
