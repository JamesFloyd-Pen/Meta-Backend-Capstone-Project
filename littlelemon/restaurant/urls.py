#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken



urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),


]
