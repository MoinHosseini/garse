from django.shortcuts import redirect
from django.urls import reverse
import re

class WhitelistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        pk = "4"
        match='11'
        match = re.search(r"\/(\d+)\/", request.path)
        if match:
            pk = match.group(1)
        checklist = [
            reverse('book:author-create'),
            reverse('book:author-update', args=[pk]),
            reverse('book:author-delete', args=[pk]),
            
            reverse('book:book-create'),
            reverse('book:book-update',args=[pk]),
            reverse('book:book-delete', args=[pk]),

            reverse('book:category-create'),
            reverse('book:category-update', args=[pk]),
            reverse('book:category-delete', args=[pk]),

            reverse('book:publisher-create'),
            reverse('book:publisher-update',args=[pk]),
            reverse('book:publisher-delete', args=[pk]),

            reverse('book:user-create'),


            reverse('book:comment-list'),
            reverse('book:comment-detail', args=[pk]),
            reverse('book:request-list'),
            reverse('book:request-detail', args=[pk]),
            reverse('book:send-email'),

        ]
        customusers = [
            reverse('book:user-profile'),
        ]


        # Check if the requested URL is in the whitelist
        if not request.user.is_superuser and request.path in checklist:
            return redirect('book:login')  # Redirect to login page for unauthorized access

        if not request.user.is_authenticated and request.path in customusers:
            return redirect('book:login')

        # Continue with the request if the user is authenticated or the URL is in the whitelist
        response = self.get_response(request)
        return response
