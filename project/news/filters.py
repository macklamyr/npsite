from django_filters import FilterSet, ModelChoiceFilter, DateFilter, ModelMultipleChoiceFilter, CharFilter
from django import forms
from .models import Post, Author, Category


class PostFilter(FilterSet):
    author = ModelMultipleChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
    )
    title = CharFilter(
        field_name='title',
        label='Заголовок',
    )
    date_in = DateFilter(
        field_name='date_in',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte',
    )
    category = ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категории',
        conjoined=True,
    )

    class Meta:
        model = Post
        fields = []
