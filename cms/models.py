# cms/models.py
from django.db import models
from django.conf import settings


# ---
# Managers
# ---

class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class FeaturedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published', is_featured=True)


# ---
# Models
# ---


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # FKs
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')
    # Model fields
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published_at')
    content = models.TextField()
    image = models.ImageField(upload_to='posts/%Y%m%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    # SEO fields
    seo_title = models.CharField(max_length=250, blank=True)
    seo_description = models.TextField(blank=True)
    seo_keywords = models.CharField(max_length=250, blank=True)
    # Other fields
    is_featured = models.BooleanField(default=False)

    # Managers
    objects = models.Manager()  # The default manager.
    published = PublishedPostManager()  # Custom manager.

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        # Sort by published_at in descending order. (newest first)
        ordering = ('is_featured', '-published_at',)
        indexes = [
            models.Index(fields=['status', 'is_featured']),
            models.Index(fields=['status', 'published_at']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # TODO: Implement get_absolute_url for Post model.
        pass


class Page(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # TODO: Implement get_absolute_url for Page model.
        pass


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # TODO: Implement get_absolute_url for Category model.
        pass


class Tag(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # TODO: Implement get_absolute_url for Tag model.
        pass
