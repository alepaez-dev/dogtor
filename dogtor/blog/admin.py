from django.contrib import admin


# Models
from . import models

# Register your models here.


# Panel de administracion para la app de 'blog'
class BlogAdminArea(admin.AdminSite):
    """Blog admin panel administration."""

    site_header = "Blog Site Admin Area"


# Instanciar nuestra clase para poderla utilizar
blog_admin_site = BlogAdminArea(name="BlogAdmin")

# Registramos modelo 'Post' en nuestro admin area
blog_admin_site.register(models.Post)

# Registrarlo en el admin area general de admin.
admin.site.register(models.Post)
