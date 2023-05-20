from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemList, MenuItemdetail, ManagersView, ManagersUserView, DeliveryCrewView, DeliveryCrew, CartView, OrderView

"""router = DefaultRouter()
router.register('users', ManagersView, basename='manager')"""



urlpatterns = [
    path('menu-items/', MenuItemList.as_view(), name='menu-item'),
    path('menu-items/<int:pk>/', MenuItemdetail.as_view(), name='item'),
    path('groups/manager/users/', ManagersView.as_view(), name='managers'),
    path('groups/manager/users/<int:id>/', ManagersUserView.as_view(), name='managers_user'),
    path('groups/delivery-crew/users/', DeliveryCrew.as_view(), name='delivery_crew'), 
    path('groups/delivery-crew/users/<int:id>/', DeliveryCrewView.as_view(), name='delivery_crew_user'),
    path('cart/menu-items/', CartView.as_view(), name='cart'),
    path('orders/', OrderView.as_view(), name='order'),
]
