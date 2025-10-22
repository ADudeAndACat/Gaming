from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
import markdown
from markdown.extensions import codehilite, toc, tables
import os


class Category(models.Model):
    """Category model for organizing content"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('content:category_detail', kwargs={'slug': self.slug})


class Page(models.Model):
    """Main content model for markdown pages"""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField(help_text="Markdown content")
    rendered_content = models.TextField(blank=True, editable=False)
    excerpt = models.TextField(max_length=500, blank=True, help_text="Short description or excerpt")
    
    # Metadata
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='pages')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    featured = models.BooleanField(default=False)
    
    # SEO fields
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    
    # File upload
    markdown_file = models.FileField(upload_to='markdown_files/', blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['category', '-created_at']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Auto-generate slug from title
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Process markdown file if uploaded
        if self.markdown_file and not self.content:
            try:
                with open(self.markdown_file.path, 'r', encoding='utf-8') as f:
                    self.content = f.read()
            except Exception as e:
                pass  # Handle file reading errors gracefully
        
        # Render markdown to HTML
        if self.content:
            md = markdown.Markdown(extensions=[
                'codehilite',
                'toc',
                'tables',
                'fenced_code',
                'nl2br',
                'sane_lists'
            ])
            self.rendered_content = md.convert(self.content)
        
        # Auto-generate excerpt if not provided
        if not self.excerpt and self.content:
            # Take first 500 characters of plain text
            plain_text = self.content.replace('#', '').replace('*', '').replace('_', '')
            self.excerpt = plain_text[:500] + '...' if len(plain_text) > 500 else plain_text
        
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('content:page_detail', kwargs={'slug': self.slug})
    
    @property
    def is_published(self):
        return self.status == 'published'
    
    @property
    def reading_time(self):
        """Estimate reading time in minutes"""
        word_count = len(self.content.split())
        return max(1, word_count // 200)  # Average 200 words per minute


class Tag(models.Model):
    """Tag model for content tagging"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class PageTag(models.Model):
    """Many-to-many relationship between Pages and Tags"""
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='page_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='page_tags')
    
    class Meta:
        unique_together = ('page', 'tag')


class Comment(models.Model):
    """Comment model for page comments"""
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Comment by {self.author_name} on {self.page.title}'
