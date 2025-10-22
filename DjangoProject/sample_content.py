#!/usr/bin/env python
"""
Script to create sample content for Django CMS testing
"""
import os
import sys
import django
from datetime import datetime

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms_project.settings')
django.setup()

from django.contrib.auth.models import User
from content.models import Category, Page, Tag, PageTag

def create_sample_content():
    """Create sample categories, tags, and pages"""
    
    # Get the admin user
    admin_user = User.objects.get(username='admin')
    
    # Create categories
    categories_data = [
        {
            'name': 'Technology',
            'description': 'Articles about technology, programming, and software development'
        },
        {
            'name': 'Tutorials',
            'description': 'Step-by-step guides and tutorials'
        },
        {
            'name': 'Documentation',
            'description': 'Project documentation and technical specifications'
        }
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        categories[cat_data['name']] = category
        if created:
            print(f"Created category: {category.name}")
    
    # Create tags
    tag_names = ['python', 'django', 'markdown', 'web-development', 'tutorial', 'guide', 'cms']
    tags = {}
    for tag_name in tag_names:
        tag, created = Tag.objects.get_or_create(name=tag_name)
        tags[tag_name] = tag
        if created:
            print(f"Created tag: {tag.name}")
    
    # Create sample pages
    pages_data = [
        {
            'title': 'Welcome to Django CMS',
            'content': '''# Welcome to Django CMS

This is a powerful content management system built with Django that supports **Markdown** formatting.

## Features

- **Markdown Support**: Write content in Markdown and see it rendered beautifully
- **Category Organization**: Organize your content with categories
- **Tag System**: Tag your content for better discoverability
- **Search Functionality**: Advanced search with filtering
- **Admin Interface**: Comprehensive admin panel for content management
- **Responsive Design**: Mobile-friendly Bootstrap-based design

## Getting Started

1. Create categories to organize your content
2. Write your content in Markdown format
3. Add tags to make content discoverable
4. Publish your content for the world to see

> This CMS makes it easy to manage and publish content with the power of Markdown!

### Code Example

```python
def hello_world():
    print("Hello from Django CMS!")
```

Enjoy using your new content management system!''',
            'category': 'Documentation',
            'tags': ['django', 'cms', 'markdown'],
            'featured': True,
            'status': 'published'
        },
        {
            'title': 'Getting Started with Markdown',
            'content': '''# Getting Started with Markdown

Markdown is a lightweight markup language that allows you to format text using simple syntax.

## Basic Syntax

### Headers
Use `#` for headers:
- `# H1`
- `## H2` 
- `### H3`

### Text Formatting
- **Bold text** with `**text**`
- *Italic text* with `*text*`
- `Code` with backticks

### Lists
Unordered lists:
- Item 1
- Item 2
- Item 3

Ordered lists:
1. First item
2. Second item
3. Third item

### Links and Images
- Links: `[Link text](URL)`
- Images: `![Alt text](image-url)`

### Code Blocks
```python
def example():
    return "This is a code block"
```

### Tables
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
| Data 3   | Data 4   |

### Blockquotes
> This is a blockquote
> It can span multiple lines

That's the basics of Markdown! Start writing and see your content come to life.''',
            'category': 'Tutorials',
            'tags': ['markdown', 'tutorial', 'guide'],
            'featured': False,
            'status': 'published'
        },
        {
            'title': 'Django CMS Architecture',
            'content': '''# Django CMS Architecture

This document outlines the architecture and design decisions behind our Django-based Content Management System.

## Core Components

### Models
- **Page**: Main content model with Markdown support
- **Category**: Content organization
- **Tag**: Content tagging system
- **Comment**: User engagement system

### Features
- Automatic Markdown to HTML conversion
- File upload support for `.md` files
- SEO optimization fields
- Reading time estimation
- Comment moderation system

## Technical Stack

- **Backend**: Django 5.2+
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Bootstrap 5.3
- **Markdown Processing**: python-markdown with extensions
- **Code Highlighting**: Prism.js

## File Structure
```
DjangoProject/
├── cms_project/          # Main project
├── content/              # Content app
│   ├── models.py        # Data models
│   ├── views.py         # View logic
│   ├── admin.py         # Admin interface
│   ├── urls.py          # URL routing
│   └── templates/       # HTML templates
├── static/              # Static files
└── media/               # Uploaded files
```

## Security Considerations
- CSRF protection enabled
- User authentication for comments
- Content moderation system
- File upload validation

This architecture provides a solid foundation for content management while maintaining flexibility and extensibility.''',
            'category': 'Documentation',
            'tags': ['django', 'python', 'web-development'],
            'featured': True,
            'status': 'published'
        }
    ]
    
    for page_data in pages_data:
        page, created = Page.objects.get_or_create(
            title=page_data['title'],
            defaults={
                'content': page_data['content'],
                'author': admin_user,
                'category': categories[page_data['category']],
                'status': page_data['status'],
                'featured': page_data['featured']
            }
        )
        
        if created:
            print(f"Created page: {page.title}")
            
            # Add tags to the page
            for tag_name in page_data['tags']:
                PageTag.objects.get_or_create(
                    page=page,
                    tag=tags[tag_name]
                )
    
    print("\nSample content created successfully!")
    print("You can now visit http://127.0.0.1:8000 to see your CMS in action!")

if __name__ == '__main__':
    create_sample_content()
