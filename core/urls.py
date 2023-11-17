from django.urls import path
from .views import home,board_page

urlpatterns = [
    path("", home, name="homepage"),
    path('boards/<str:board_name>', board_page, name="board_page")
]
