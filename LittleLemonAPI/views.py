from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from rest_framework import status
from rest_framework.views import APIView
from .models import Category, MenuItems, Cart, Order, OrderItems
from .serializers import CategorySerializer, MenuItemSerializer, ManagerSerializer, CartSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsManager,  ManagerPermission
from django.contrib.auth.models import User, Group

    
class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManager]
    
class MenuItemdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManager]
    
    
class ManagersView(APIView):
    permission_classes = [ManagerPermission]
    def get(self, request):
        try:
            manager_group = Group.objects.get(name='Manager')
            manager_users = manager_group.user_set.all()
        except Group.DoesNotExist:
            return Response("Manager group does not exist", status=status.HTTP_404_NOT_FOUND)
        serializer = ManagerSerializer(manager_users, many=True)
        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            id = request.POST.get('id')
            user = User.objects.get(id=id)
        except Exception:
            return Response({"Message":"User Not found"}, status=status.HTTP_404_NOT_FOUND)
        group = Group.objects.get(name='Manager')
        user.groups.add(group)
        return Response({"Message":"success"}, status=status.HTTP_201_CREATED)
    

class ManagersUserView(APIView):
    permission_classes = [ManagerPermission]
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            group = get_object_or_404(Group, name='Manager')
        except Exception:
            return Response({"Message":"User Not found"}, status=status.HTTP_404_NOT_FOUND)
        user.groups.remove(group)
        return Response({"Message":"success"}, status=status.HTTP_200_OK)
    

class DeliveryCrew(APIView):
    permission_classes = [IsManager]
    def get(self, request):
        try:
            delivery_crew_group = Group.objects.get(name='Delivery_crew')
            delivery_crew_users = delivery_crew_group.user_set.all()
        except Group.DoesNotExist:
            return Response("Delivery_crew group not found", status=status.HTTP_404_NOT_FOUND)
        serializer = ManagerSerializer(delivery_crew_users, many=True)
        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            id = request.POST.get('id')
            user = User.objects.get(id=id)
        except Exception:
            return Response({"Message":"User Not found"}, status=status.HTTP_404_NOT_FOUND)
        group = Group.objects.get(name='Delivery_crew')
        user.groups.add(group)
        return Response({"Message":"success"}, status=status.HTTP_201_CREATED)
    

class DeliveryCrewView(APIView):
    permission_classes = [IsManager]
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            group = get_object_or_404(Group, name='Delivery_crew')
        except Exception:
            return Response({"Message":"User Not found"}, status=status.HTTP_404_NOT_FOUND)
        user.groups.remove(group)
        return Response({"Message":"success"}, status=status.HTTP_200_OK)
    

class CartView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Cart.objects.filter(user=user)
        return queryset
    

    
class OrderView(APIView):
    def get(self, request):
        user = self.request.user
        queryset = Order.objects.filter(user=user).prefetch_related('orderitem')
        serializer = OrderSerializer(queryset, many=True)
        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        
        order = Order(
            user=user,
            status=False,
            total=0,
        )
        order.save()
        for cart_item in cart_items:
            order_item = OrderItems(
                order=order,
                menuitem=cart_item.menuitem,
                quantity=cart_item.quantity,
                unit_price=cart_item.unit_price,
                price=cart_item.price
            )
            order.total += order_item.price
            order_item.save()
            order.save()
        cart_items.delete()
        
        return Response("Order items created and cart items deleted successfully.")
    
