from django.contrib import admin
from  .models import FoodCategory, Food, FoodSerializer, FoodListSerializer
# Register your models here.

admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(FoodSerializer)
admin.site.register(FoodListSerializer)