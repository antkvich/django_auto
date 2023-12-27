from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path("showrooms/", views.ShowroomListView.as_view()),
    path("showrooms/<int:pk>/", views.ShowroomDetailView.as_view()),
    path("discounts/", views.DiscountListView.as_view()),
    path("discounts/<int:pk>", views.DiscountDetailView.as_view()),
    path("cars/", views.CarListView.as_view()),
    path("cars/<int:pk>", views.CarDetailView.as_view()),
]

formatted_urlpatterns = format_suffix_patterns(urlpatterns)
