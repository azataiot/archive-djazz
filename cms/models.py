# cms/models.py
from django.conf import settings
from django.db import models


# ---
# Managers
# ---

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class FeaturedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published', is_featured=True)


# ---
# Models
# ---


class BaseModel(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published_at')
    description = models.TextField(max_length=250, blank=True)
    keywords = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel, models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # FKs
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')
    # Model fields
    content = models.TextField()
    image = models.ImageField(upload_to='posts/%Y%m%d/', blank=True)
    published_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)

    # Managers
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Custom manager.
    featured = FeaturedManager()  # Custom manager.

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


class Page(BaseModel, models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    content = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # Managers
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Custom manager.

    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # TODO: Implement get_absolute_url for Page model.
        pass


class Category(BaseModel, models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # TODO: Implement get_absolute_url for Category model.
        pass


class Tag(BaseModel, models.Model):
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # TODO: Implement get_absolute_url for Tag model.
        pass
