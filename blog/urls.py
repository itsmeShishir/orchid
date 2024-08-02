from django.urls import path
from blog import views
urlpatterns = [
   path("blog/", views.BlogPage),
   path("blog/<int:pk>/", 
        views.SingleBlog, name="singleblog")
]
