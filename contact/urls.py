from django.urls import path
from contact import views
urlpatterns = [
   path("contact/", views.contact_us, name="contact"),
   path("login/", views.login_view, name="login"),
   path("register/", views.register_view, name="register"),
   path("logout/", views.logout_view, name="logout"),
   path("contact/update/<int:pk>/", views.contactUpdate_view, name="updateContact"),
   path("contact/delete/<int:pk>/", views.contactDelete_view, name="deleteContact"),
   path('allContact/', views.allContact_view, name="allContact"),
   path('addCategory/', views.all_category, name="addCategory")
]
