from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView


# Models
from vet.models import PetOwner, Pet


# Create your views here.
def list_pet_owners(request):
    # por defecto -> metodo GET
    print("REQUEST --->", request.__dict__)

    """List owners."""

    # Agarrar informacion de nuestra bd
    owners = PetOwner.objects.all()

    # Hacemos el contexto
    context = {"owners": owners}

    # Agarrar template
    template = loader.get_template("vet/owners/list.html")

    # Retornar respuesta HTTP con el template pasandole el contexto y el request
    return HttpResponse(template.render(context, request))


# CRUD


# Ctrl + /
# Cmd + /
class OwnersList(TemplateView):
    # Renderizame este template
    template_name = "vet/owners/list.html"

    # Que este template va a tener cierto 'contexto'
    def get_context_data(self, **kwargs):
        # Agarrar el contexto que ya creo 'TemplateView'
        context = super().get_context_data(**kwargs)

        # Le agregamos nuestro custom context
        context["owners"] = PetOwner.objects.all()
        return context


class PetsList(TemplateView):
    # Renderizame este template
    template_name = "vet/pets/list.html"

    # Que este template va a tener cierto 'contexto'
    def get_context_data(self, **kwargs):
        # Agarrar el contexto que ya creo 'TemplateView'
        context = super().get_context_data(**kwargs)

        # Le agregamos nuestro custom context
        context["pets"] = Pet.objects.all()
        return context


class PetsDetail(TemplateView):
    # Renderizame este template
    template_name = "vet/pets/detail.html"

    # Que este template va a tener cierto 'contexto'
    def get_context_data(self, **kwargs):
        # Agarrar el contexto que ya creo 'TemplateView'

        context = super().get_context_data(**kwargs)

        # Le agregamos nuestro custom context
        context["pet"] = Pet.objects.get(pk=kwargs["pk"])
        return context


class OwnersList(ListView):
    """Render all Pet Owners."""

    # 1. Modelo que estamos manipulando
    # 2. Template con el que vamos renderizar
    # 3. El contexto que va a tener ese template
    model = PetOwner  # 1
    template_name = "vet/owners/list.html"  # 2
    context_object_name = "owners"  # 3


class OwnerDetail(DetailView):
    """Render a specific Pet Owner with their pk."""

    # 1. Modelo
    # 2. Template a renderizar
    # 3. El contexto que va a tener ese template
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"


class Test(View):
    # Como funcion el metodo(GET,PATCH,POST,DELETE,PUT)
    def get(self, request):
        return HttpResponse("Hello world from a class generic view")
