from django.urls import path
from blog_api.views.authorViews import AuthorView, AuthorDetail

urlpatterns = [
    path('', AuthorView.as_view()),
    path('<str:pk>', AuthorDetail.as_view()),
]