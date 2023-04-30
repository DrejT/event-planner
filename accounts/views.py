from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView
from .models import UserPost
from .forms import CustomUserCreationForm, PostForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class PostView(CreateView):
    form_class = PostForm
    success_url = reverse_lazy("home")
    template_name= "new_post.html"
    context_object_name = "search_results"

    def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)

class HomePageView(ListView):
    context_object_name = "search_results"
    model= UserPost
    template_name = "home.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return UserPost.objects.filter(title__icontains=query)
        else:
            return 0

class DetailPostView(DetailView):
    model = UserPost
    paginate_by = 3
    template_name = "detail_post.html"
