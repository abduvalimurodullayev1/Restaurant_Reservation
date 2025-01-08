from django_filters import rest_framework as filters
from .models import Restaurant


class RestaurantFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = Restaurant
        fields = ['title']