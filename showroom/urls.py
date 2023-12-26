from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path("showrooms/", views.ShowroomList.as_view()),
    path("showrooms/<int:pk>/", views.ShowroomDetail.as_view()),
]

formatted_urlpatterns = format_suffix_patterns(urlpatterns)
