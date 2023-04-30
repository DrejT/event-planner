from django.urls import path
from .models import UserPost
from .views import SignUpView, PostView, DetailPostView
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("new/", PostView.as_view(), name="post"),
    path("<int:pk>/", DetailPostView.as_view(), name= "detailpost")
]
