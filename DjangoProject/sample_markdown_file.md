# Advanced Django Features

This is a sample markdown file that demonstrates the file upload functionality of our Django CMS system.

## Overview

When you upload this markdown file through the admin interface, the CMS will automatically:

1. **Read the file content** and populate the content field
2. **Convert Markdown to HTML** using python-markdown
3. **Generate a slug** from the title
4. **Estimate reading time** based on word count
5. **Create an excerpt** if none is provided

## Code Examples

Here's a Python function that demonstrates Django model usage:

```python
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

## Features Demonstrated

### Text Formatting
- **Bold text** for emphasis
- *Italic text* for subtle emphasis
- `Inline code` for technical terms

### Lists and Structure
1. Ordered lists for step-by-step instructions
2. Unordered lists for feature highlights
3. Nested content organization

### Advanced Elements

> This is a blockquote that will be styled beautifully in the rendered HTML.
> It can contain multiple lines and will maintain proper formatting.

### Tables

| Feature | Status | Description |
|---------|--------|-------------|
| Markdown Support | ✅ Complete | Full markdown rendering |
| File Upload | ✅ Complete | Direct .md file upload |
| Admin Interface | ✅ Complete | Comprehensive management |
| Search | ✅ Complete | Advanced filtering |

## Mathematical Expressions

If you have the math extension enabled, you can include mathematical expressions:

The quadratic formula: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

## Conclusion

This sample file demonstrates the power and flexibility of our Django CMS system. Upload this file through the admin interface to see how it automatically processes and renders the content!

---

*This file was created to test the markdown file upload functionality of Django CMS.*
