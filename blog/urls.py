from django.urls import path
from django.conf.urls import url
from .views import( 
  PostListView,
  PostDetailView,
  PostCreateView,
  PostUpdateView,
  PostDeleteView,
  UserPostListView
)
from . import views
 
urlpatterns = [
    url(r'^$',  PostListView.as_view() , name='blog-name'),
    path('user/<str:username>',  UserPostListView.as_view() , name='user-posts'),
    url(r'^post/(?P<pk>\d+)/$',  PostDetailView.as_view() , name='post-detail'),
    url(r'^post/new/$' ,  PostCreateView.as_view() , name='post-create'),
    url(r'^post/(?P<pk>\d+)/update/$',  PostUpdateView.as_view() , name='post-update'),
    url(r'^post/(?P<pk>\d+)/delete/$',  PostDeleteView.as_view() , name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
