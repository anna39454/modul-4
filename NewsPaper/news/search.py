from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
import django_filters
from .models import Post
from django_filters import FilterSet, DateFilter
from django import forms

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):

    data = DateFilter(
        field_name='dateCreation',
        widget=forms.DateInput(attrs={'type': 'date'}),
        lookup_expr='date__gte',
    )
    class Meta:

        model = Post
         # В fields мы описываем по каким полям модели
         # будет производиться фильтрация.
        fields = {
            'postCategory': ['exact'],
            'tile': ['icontains'],


       }