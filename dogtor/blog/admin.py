from django.contrib import admin


# Models
# from . import models -> importamos todos los modelos

# Importamos especificamente los modelos que le decimos
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin model for admin."""

    fields = ["name"]


# SITIO -> Panel de administracion para la app de 'blog'
class BlogAdminArea(admin.AdminSite):
    """Blog admin panel administration."""

    site_header = "Blog Site Admin Area"


# Instanciar nuestra clase para poderla utilizar
blog_admin_site = BlogAdminArea(name="BlogAdmin")
