from django.urls import path
from .views import (
    home_view,BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    PublisherListView, PublisherDetailView, PublisherCreateView, PublisherUpdateView, PublisherDeleteView,
    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    BookByAuthorView,BooksByPublisherView,BooksByCategoryView,CustomLoginView,
    comment_submit,like_book, CommentListView,CommentDetailView,comment_status,
    RequestListView,RequestDetailView,request_status,send_email,
    SignUp,user_profile,
    )
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'book'

urlpatterns = [
    path('', home_view, name='home'),
    path('users/create', SignUp.as_view(), name="user-create" ),
    path('users/profile', user_profile, name='user-profile'),
    
    

   
    path('books/by-author/', BookByAuthorView.as_view(), name='books-by-author'),
    path('books-by-publisher/', BooksByPublisherView.as_view(), name='books-by-publisher'),
    path('books-by-category/', BooksByCategoryView.as_view(), name='books-by-category'),
    
    path('login/', auth_views.LoginView.as_view(template_name='book/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='book/login.html'), name='logout'),


    # Book URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),

    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),

    # Publisher URLs
    path('publishers/', PublisherListView.as_view(), name='publisher-list'),
    path('publishers/create/', PublisherCreateView.as_view(), name='publisher-create'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher-detail'),
    path('publishers/update/<int:pk>/', PublisherUpdateView.as_view(), name='publisher-update'),
    path('publishers/delete/<int:pk>/', PublisherDeleteView.as_view(), name='publisher-delete'),

    # Author URLs
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/update/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author-delete'),

    path('comment/submit', comment_submit, name='comment-submit'),
    path('like-book/<int:book_id>/', like_book, name='like-book'),

    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('comment/<int:pk>/', comment_status, name='comment-status'),


    path('requests/', RequestListView.as_view(), name='request-list'),
    path('requests/<int:pk>/', RequestDetailView.as_view(), name='request-detail'),
    path('request/<int:pk>/', request_status, name='request-status'),

    path('sendmail', send_email, name='send-email'),

]
