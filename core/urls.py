from django.urls import path
from .views import home,board_page_scroll,board_page_catalog,single_thread,delete_post

urlpatterns = [
    path("", home, name="homepage"),
    path('boards/<str:board_name>', board_page_scroll, name="board_page"),
    path('boards/<str:board_name>/catalog', board_page_catalog, name="board_page_cat"),
    path('boards/<str:board_name>/thread/<int:thread_id>/', single_thread, name='single_thread'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]

handler404 = 'core.views.page404'
