from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('pages/', views.PageListView.as_view(), name='page_list'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tag/<slug:slug>/', views.tag_detail_view, name='tag_detail'),
    path('search/', views.search_view, name='search'),
    path('comment/<slug:page_slug>/', views.add_comment, name='add_comment'),
]
