from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path("showrooms/", views.ShowroomList.as_view()),
    path("showrooms/<int:pk>/", views.ShowroomDetail.as_view()),
    path("discounts/", views.DiscountList.as_view()),
    path("discounts/<int:pk>", views.DiscountDetail.as_view()),
    path("cars/", views.CarList.as_view()),
    path("cars/<int:pk>", views.CarDetail.as_view()),
]

formatted_urlpatterns = format_suffix_patterns(urlpatterns)
