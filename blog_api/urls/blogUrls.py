from django.urls import path
from  blog_api.views.blogViews import Blogs, BlogDetail

urlpatterns = [
    path('', Blogs.as_view()),
    path('<str:pk>', BlogDetail.as_view()),
]