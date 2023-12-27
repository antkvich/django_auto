from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from supplier import views


urlpatterns = [
    path("suppliers/", views.SupplierListView.as_view()),
    path("suppliers/<int:pk>", views.SupplierDetailView.as_view()),
]

formatted_urlpatterns = format_suffix_patterns(urlpatterns)
