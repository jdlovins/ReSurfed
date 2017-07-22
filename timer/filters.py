from django_filters import rest_framework as filters
from .models import Map, Time


class MapFilter(filters.FilterSet):
    min_d = filters.NumberFilter(name="difficulty", lookup_expr='gte')
    max_d = filters.NumberFilter(name="difficulty", lookup_expr='lte')

    class Meta:
        model = Map
        fields = '__all__'


class TimeFilter(filters.FilterSet):

    class Meta:
        model = Time
        fields = '__all__'