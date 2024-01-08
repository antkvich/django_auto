from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from customer import views


urlpatterns = [
    path("offers/", views.PurchaseOfferListView.as_view()),
    path("offers/<int:pk>", views.PurchaseOfferDetailView.as_view()),
    path("customers/", views.CustomerListView.as_view()),
    path("customers/<int:pk>", views.CustomerOfferDetail.as_view()),
]

formatted_urlpatterns = format_suffix_patterns(urlpatterns)
