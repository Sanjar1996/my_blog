from django.urls import path

from .views import (
    BlogListView,
    BlogDetail,
    BlogCreate,
    BlogUpdate,
    BlogDelete
)

urlpatterns = [
    path('blog/<int:pk>/delete', BlogDelete.as_view(), name='post_delete'),
    path('blog/<int:pk>/edit', BlogUpdate.as_view(), name='post_edit'),
    path('blog/new', BlogCreate.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail')
]
