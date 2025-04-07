from django.urls import path # type: ignore
from . import views
from .views import recommend_fertilizer  # Import the view
from .views import register_farmer
from .views import order_fertilizer


urlpatterns = [
       path('', views.home, name='home'),  # Add homepage route
   path('register/', register_farmer, name='register_farmer'),
      path('recommend/', recommend_fertilizer, name='recommend_fertilizer'),  # ✅ URL Pattern

      path('orders/', order_fertilizer, name='order_fertilizer'),
       path('order_success/', views.order_success, name='order_success'),
]
