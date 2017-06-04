from girox.advertising.mixins import ListViewAdvertiser, DetailViewAdvertiser
from girox.blog.models import Post


post_list = ListViewAdvertiser.as_view(model=Post)

post_detail = DetailViewAdvertiser.as_view(model=Post)
