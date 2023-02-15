from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_list.as_view(), name='blogs-page'),
    path('<pk>', views.blog_detail.as_view(), name='blog-detail-page'),
    path('blog-comment/', views.blog_comment.as_view(), name='blog-comment'),
]


