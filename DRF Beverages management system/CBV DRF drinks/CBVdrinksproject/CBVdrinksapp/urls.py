from django.contrib import admin
from django.urls import path
# from .views import DrinksListView,DrinksDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
#     path('drinks/',DrinksListView.as_view()),
#     path('drinks/<int:pk>',DrinksDetailView.as_view()),
]
