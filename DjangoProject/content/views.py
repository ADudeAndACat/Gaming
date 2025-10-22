from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Page, Category, Tag, Comment


class PageListView(ListView):
    """List view for published pages"""
    model = Page
    template_name = 'content/page_list.html'
    context_object_name = 'pages'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Page.objects.filter(status='published').select_related('author', 'category')
        
        # Search functionality
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(excerpt__icontains=search_query)
            )
        
        # Category filter
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        # Tag filter
        tag_slug = self.request.GET.get('tag')
        if tag_slug:
            queryset = queryset.filter(page_tags__tag__slug=tag_slug)
        
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['search_query'] = self.request.GET.get('search', '')
        context['current_category'] = self.request.GET.get('category', '')
        context['current_tag'] = self.request.GET.get('tag', '')
        return context


class PageDetailView(DetailView):
    """Detail view for individual pages"""
    model = Page
    template_name = 'content/page_detail.html'
    context_object_name = 'page'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        return Page.objects.filter(status='published').select_related('author', 'category')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.get_object()
        
        # Get related pages (same category)
        context['related_pages'] = Page.objects.filter(
            category=page.category,
            status='published'
        ).exclude(id=page.id)[:3]
        
        # Get page tags
        context['page_tags'] = Tag.objects.filter(page_tags__page=page)
        
        # Get approved comments
        context['comments'] = Comment.objects.filter(
            page=page,
            is_approved=True
        ).order_by('-created_at')
        
        return context


class CategoryDetailView(DetailView):
    """Detail view for categories showing all pages in that category"""
    model = Category
    template_name = 'content/category_detail.html'
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        
        # Get pages in this category with pagination
        pages = Page.objects.filter(
            category=category,
            status='published'
        ).select_related('author').order_by('-created_at')
        
        paginator = Paginator(pages, 10)
        page_number = self.request.GET.get('page')
        context['pages'] = paginator.get_page(page_number)
        
        return context


def home_view(request):
    """Home page view"""
    featured_pages = Page.objects.filter(
        status='published',
        featured=True
    ).select_related('author', 'category')[:3]
    
    recent_pages = Page.objects.filter(
        status='published'
    ).select_related('author', 'category').order_by('-created_at')[:6]
    
    categories = Category.objects.all()[:6]
    
    context = {
        'featured_pages': featured_pages,
        'recent_pages': recent_pages,
        'categories': categories,
    }
    
    return render(request, 'content/home.html', context)


def search_view(request):
    """Advanced search view"""
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    tag_id = request.GET.get('tag', '')
    
    pages = Page.objects.filter(status='published')
    
    if query:
        pages = pages.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(excerpt__icontains=query)
        )
    
    if category_id:
        pages = pages.filter(category_id=category_id)
    
    if tag_id:
        pages = pages.filter(page_tags__tag_id=tag_id)
    
    pages = pages.select_related('author', 'category').distinct()
    
    # Pagination
    paginator = Paginator(pages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'pages': page_obj,
        'query': query,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'selected_category': category_id,
        'selected_tag': tag_id,
    }
    
    return render(request, 'content/search.html', context)


@login_required
def add_comment(request, page_slug):
    """Add comment to a page (AJAX)"""
    if request.method == 'POST':
        page = get_object_or_404(Page, slug=page_slug, status='published')
        
        author_name = request.POST.get('author_name', '')
        author_email = request.POST.get('author_email', '')
        content = request.POST.get('content', '')
        
        if author_name and author_email and content:
            comment = Comment.objects.create(
                page=page,
                author_name=author_name,
                author_email=author_email,
                content=content,
                is_approved=False  # Require approval
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Comment submitted successfully. It will be reviewed before publication.'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'All fields are required.'
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def tag_detail_view(request, slug):
    """View for displaying pages with a specific tag"""
    tag = get_object_or_404(Tag, slug=slug)
    
    pages = Page.objects.filter(
        page_tags__tag=tag,
        status='published'
    ).select_related('author', 'category').order_by('-created_at')
    
    # Pagination
    paginator = Paginator(pages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'tag': tag,
        'pages': page_obj,
    }
    
    return render(request, 'content/tag_detail.html', context)
