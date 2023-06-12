from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from restaurant.models import Menu, Booking
from restaurant.serializers import BookingSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
