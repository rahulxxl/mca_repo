import django_filters
from django_filters import DateFilter

from . import models

# class OrderFilter(django_filters.FilterSet):
#     # gte is greater than or equal to
#     start_date = django_filters.DateFilter(field_name="date_created", lookup_expr="gte")
#     # lte is lesser than or equal to
#     start_date = django_filters.DateFilter(field_name="date_created", lookup_expr="lte")
#     class Meta:
#         model=models.Artist
#         fields ='__all__'
#         exclude= ['customer', 'date_created']
