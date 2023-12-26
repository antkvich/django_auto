from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path("offers/", views.PurchaseOfferList.as_view()),
    path("offers/<int:pk>", views.PurchaseOfferDetail.as_view()),
]

formatted_urlpatterns = format_suffix_patterns(urlpatterns)
