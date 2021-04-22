from django.urls import path

from .views import BookmarkListView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),  # html file - {% url 'bookmark:list' %}
]