from django.urls import path

# DRF imports
from .views import CreateAppUserView, ListAppUserView

# Vanilla Django imports
from .views import home_view


urlpatterns = [
    path('', ListAppUserView.as_view()),
    path('new_user', CreateAppUserView.as_view()),
    path('home', home_view)
]
