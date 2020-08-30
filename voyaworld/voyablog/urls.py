
from django.contrib import admin
from django.urls import path
from voyablog import views
app_name='voyablog'
urlpatterns = [
    path('blog/',views.blog.as_view(),name='blog'),
    path('blog/<int:pk>',views.BlogDetail.as_view(),name='BlogDetail'),
    path('Gallery/',views.Gallery,name='gallery'),
    path('add-blog/',views.add_blog),
    # path('/profile/edit/<int:pk>/', views.ProfileUpdateView.as_view(success_url="/voyablog/blog")),
    path('profile/edit/<int:pk>/', views.ProfileUpdateView ,name='ProfileUpdateView'),
    path('profile/detail/<int:pk>', views.ProfileDetailView.as_view()),
]
