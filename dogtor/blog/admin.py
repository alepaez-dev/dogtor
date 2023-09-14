from django.contrib import admin


# Models
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """Post Admin model for admin."""

    fields = ["name"]


# SITIO -> Panel de administracion para la app de 'blog'
class BlogAdminArea(admin.AdminSite):
    """Blog admin panel administration."""

    site_header = "Blog Site Admin Area"


# Instanciar nuestra clase para poderla utilizar
blog_admin_site = BlogAdminArea(name="BlogAdmin")

# Registramos modelo 'Post' en nuestro admin area
blog_admin_site.register(Post, PostAdmin)

# Registrarlo en el admin area general de admin.
admin.site.register(Post, PostAdmin)
