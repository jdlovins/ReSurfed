from django_filters import rest_framework as filters
from .models import Map


class MapFilter(filters.FilterSet):
    min_d = filters.NumberFilter(name="difficulty", lookup_expr='gte')
    max_d = filters.NumberFilter(name="difficulty", lookup_expr='lte')

    class Meta:
        model = Map
        fields = '__all__'

        