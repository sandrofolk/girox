from django.views.generic import ListView, DetailView
from girox.blog.models import Post


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)
