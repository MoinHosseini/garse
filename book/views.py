from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView , View
from django.urls import reverse_lazy
from .models import Category, Publisher, Author, Book
from django.shortcuts import redirect, render, get_object_or_404

from hcaptcha.fields import hCaptchaField
from django.contrib.auth import views as auth_views

from django.views.generic.edit import CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as auth_views

class CustomLoginView(LoginView):
    template_name = 'book/login.html'
    extra_context = {'hcaptcha': hCaptchaField()}

    def form_valid(self, form):
        # Mark the user as authenticated
        self.request.user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, form.get_user())
        return super().form_valid(form)



def home_view(request):
    return render(request, 'book/index.html')

from django.views.generic import ListView
from .models import Book, Category

from django.shortcuts import render
from django.views import View
from .models import Category, Book

class BooksByCategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'book/books_by_category.html', context)

    def post(self, request):
        selected_category_id = request.POST.get('category')
        books = Book.objects.filter(genre_id=selected_category_id)
        categories = Category.objects.all()
        context = {
            'books': books,
            'categories': categories
        }
        return render(request, 'book/books_by_category.html', context)



class BooksByPublisherView(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        context = {
            'publishers': publishers
        }
        return render(request, 'book/books_by_publisher.html', context)

    def post(self, request):
        selected_publisher_id = request.POST.get('publisher')
        books = Book.objects.filter(publisher_id=selected_publisher_id)
        publishers = Publisher.objects.all()  # Retrieve all publishers to render the dropdown again
        context = {
            'books': books,
            'publishers': publishers  # Pass the publishers queryset to the template
        }
        return render(request, 'book/books_by_publisher.html', context)


class BookByAuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        context = {
            'authors': authors
        }
        return render(request, 'book/books_by_author.html', context)

    def post(self, request):
        selected_author_id = request.POST.get('author')
        books = Book.objects.filter(author_id=selected_author_id)
        authors = Author.objects.all()  # Retrieve all publishers to render the dropdown again
        context = {
            'books': books,
            'authors': authors  # Pass the publishers queryset to the template
        }
        return render(request, 'book/books_by_author.html', context)


# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'category_list'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category/category_create.html'
    fields = '__all__'
    success_url = reverse_lazy('book:category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category/category_update.html'
    fields = '__all__'
    context_object_name = 'category'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category-list')





# Publisher Views
class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher/publisher_list.html'
    context_object_name = 'publisher_list'

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'publisher/publisher_detail.html'
    context_object_name = 'publisher'

class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'publisher/publisher_create.html'
    fields = '__all__'
    success_url = reverse_lazy('book:publisher-list')

class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'publisher/publisher_update.html'
    fields = '__all__'
    context_object_name = 'publisher'
    success_url = reverse_lazy('publisher-list')

class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publisher/publisher_delete.html'
    context_object_name = 'publisher'
    success_url = reverse_lazy('publisher-list')





# Author Views
class AuthorListView(ListView):
    model = Author
    template_name = 'author/author_list.html'
    context_object_name = 'author_list'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_detail.html'
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author/author_create.html'
    fields = '__all__'
    success_url = reverse_lazy('book:author-list')
    
class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author/author_update.html'
    fields = '__all__'
    context_object_name = 'author'
    success_url = reverse_lazy('author-list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/author_delete.html'
    context_object_name = 'author'
    success_url = reverse_lazy('author-list')





# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book_list'



from django.contrib.auth.mixins import LoginRequiredMixin

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = context['book']
        user = self.request.user

        context["total_likes"] = book.likes


        # Check if the user is logged in and if the book is in the user's liked books list
        if user.is_authenticated:
            liked_books = user.liked_books or {}  # Initialize as an empty list if not set
            context['user_has_liked'] = str(book.pk) in liked_books.keys()
        return context



from django.contrib.messages.views import SuccessMessageMixin

class BookCreateView(SuccessMessageMixin, CreateView):
    model = Book
    template_name = 'book/book_create.html'
    fields = ['title', 'author', 'genre', 'publication_date', 'isbn', 'description',
           'price', 'cover_image', 'publisher', 'language', 'page_count', 'average_rating', 'is_available']
    success_url = reverse_lazy('book:book-list')
    success_message = 'The book has been created successfully.'

    def form_valid(self, form):
        if form.is_valid():
            # Save the form data and assign the uploaded image
            book = form.save(commit=False)
            book.cover_image = self.request.FILES.get('cover_image')
            book.save()
            return super().form_valid(form)
        else:
            print("check")
            print(form.errors)  # Print form errors for debugging
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['genres'] = Category.objects.all()
        context['publishers'] = Publisher.objects.all()
        return context



class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book/book_update.html'
    fields = '__all__'
    context_object_name = 'book'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book:book-list')





# --------------------------
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUp(generic.CreateView):
    
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "user/user_form.html"




def user_profile(request):
    user = request.user
    books = user.liked_books.values()
    l = []
    for book in books:
        l.append( Book.objects.get(title=book) )
    return render(request, 'user/user_profile.html', {'user': user , "books":l})





from django.shortcuts import render, redirect
from .models import Comment
from django.utils import timezone
from django.http import HttpResponse

def comment_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        text = request.POST.get('text')
        
        # Create and save the comment
        print("123456789123456789123456789")
        comment = Comment(name=name, email=email, text=text, date=timezone.now())
        comment.save()
        
        # Redirect to a success page or any other desired page
        return render(request, "book/index.html")  # You can replace this with a redirect to a success page

    return HttpResponse("Invalid request method")  # Handle GET requests here


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

def like_book(request, book_id):
    # Get the book and user
    book = Book.objects.get(id=book_id)
    print(book)
    print(book.likes)
    user = request.user

    # liked_books = user.liked_books or {}
    
    if str(book_id) in user.liked_books.keys():
        del user.liked_books[str(book_id)]
        book.likes -= 1
    else:
        # Like the book
        user.liked_books[book_id] = book.title
        book.likes += 1

    # Save the user to update liked_books field
    user.save()
    book.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



from .models import Comment
from django.views.generic import ListView, DetailView


class CommentListView(ListView):
    model = Comment
    template_name = 'comment/comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        filter_param = self.request.GET.get('filter')
        queryset = super().get_queryset()

        if filter_param == 'approved':
            queryset = queryset.filter(status=True)
        elif filter_param == 'pending':
            queryset = queryset.filter(status=False)

        return queryset


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment/comment_detail.html'  # Create an HTML template for displaying a comment's details
    context_object_name = 'comment'  # Use this variable in the template to access the comment

def comment_status(request,pk):
    if request.method == 'POST':
        print("hi")
        comment = Comment.objects.get(id = pk)
        comment.status = not comment.status
        comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



from django.views.generic import ListView, DetailView
from .models import Request

class RequestListView(ListView):
    model = Request
    template_name = 'request/request_list.html'
    context_object_name = 'requests'  # Use this variable in the template
    
    def get_queryset(self):
        filter_param = self.request.GET.get('filter')
        queryset = super().get_queryset()

        if filter_param == 'approved':
            queryset = queryset.filter(status=True)
        elif filter_param == 'pending':
            queryset = queryset.filter(status=False)
        return queryset

class RequestDetailView(DetailView):
    model = Request
    template_name = 'request/request_detail.html'
    context_object_name = 'request'  # Use this variable in the template



def request_status(request,pk):
    if request.method == 'POST':
        print("hi")
        req = Request.objects.get(id = pk)
        req.status = not req.status
        req.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




# views.py
from django.shortcuts import render, redirect
from .forms import EmailForm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(request):
    if request.method == 'POST':
        # If it's a POST request, process the form data
        form = EmailForm(request.POST)
        if form.is_valid():
            sender_email = "moinceuis8@gmail.com"
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            users = CustomUser.objects.all()
            for user in users:
                receiver_email = user.email

                # Email details

                # SMTP server configuration
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                smtp_username = "moinceuis8@gmail.com"
                smtp_password = "zwimnchktonrcgcp"

                # Create the email
                email = MIMEMultipart()
                email["From"] = sender_email
                email["To"] = receiver_email
                email["Subject"] = subject

                email.attach(MIMEText(message, "plain"))

                # Create a secure connection to the SMTP server
                smtp = smtplib.SMTP(smtp_server, smtp_port)
                smtp.starttls()

                # Login to the SMTP server
                smtp.login(smtp_username, smtp_password)

                # Send the email
                smtp.sendmail(sender_email, receiver_email, email.as_string())

                # Close the SMTP connection
                smtp.quit()

                print("Email sent successfully!")
            return redirect('book:user-list')  # Redirect to a success page after sending the email
    else:
        # If it's a GET request, render the form
        form = EmailForm()

    return render(request, "user/email.html", {'form': form})

