from django.urls import path
from . import views
from .views import BookView, SingleBookView

urlpatterns = [
    path('book',views.books, name='books'),
    # path('books/<int:pk>',views.book),
    path('books', BookView.as_view(), name = 'BookView'),
    path('books/<int:pk>', views.SingleBookView.as_view(), name = 'SingleBook')
]