from django.db.models import Prefetch, Count, Q
from rest_framework import generics
from .models import Food, FoodCategory
from .serializers import FoodSerializer, FoodListSerializer



class FoodAPIView(generics.ListAPIView):
    serializer_class = FoodListSerializer
    def get_queryset(self):
        return FoodCategory.objects.prefetch_related().filter(food__is_publish=True).distinct()


# class FoodAPIView(generics.ListAPIView):
#     serializer_class = FoodListSerializer
#     def get_queryset(self):
#         """ Выборка только опубликованных блюд(но публикует ещё и пустые категории)"""
#         published_foods = Food.objects.filter(is_publish=True)
#         return FoodCategory.objects.prefetch_related(Prefetch('food', queryset=published_foods))