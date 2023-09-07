from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View, TemplateView


# Models
from vet.models import PetOwner


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


# PascalCase


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


class Test(View):
    # Como funcion el metodo(GET,PATCH,POST,DELETE,PUT)
    def get(self, request):
        return HttpResponse("Hello world from a class generic view")
