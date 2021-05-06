from django.urls import path

from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),  # html file - {% url 'bookmark:list' %}
    path('add/', BookmarkCreateView.as_view(), name='add'),   # html file - {%url 'bookmark:add' %}
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
]