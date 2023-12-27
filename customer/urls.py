from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path("offers/", views.PurchaseOfferListView.as_view()),
    path("offers/<int:pk>", views.PurchaseOfferDetailView.as_view()),
]

formatted_urlpatterns = format_suffix_patterns(urlpatterns)
