from django.urls import path
from restaurant.views import index, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", index, name='home'),
    path('items/', MenuItemsView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
