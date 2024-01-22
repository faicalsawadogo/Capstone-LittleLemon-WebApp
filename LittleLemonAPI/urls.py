from django.urls import path
from . import views
from .views import (RegisterView, CategoryView, BookingView)

urlpatterns = [
    path('users/', RegisterView.as_view(), name='register'),

    # Categories
    path('categories/', CategoryView.as_view(), name='categories'),

    # Menu Items
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:menuItem>', views.SingleMenuItemView.as_view()),

    # Bookings
    path('bookings', views.BookingView.as_view()),
]