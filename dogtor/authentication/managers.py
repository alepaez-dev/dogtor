from django.contrib.auth.models import BaseUserManager


class ModUserManager(BaseUserManager):
    """Mod User Custom Manager."""

    def create_user(self, email, user_name, first_name, password, **other_fields):
        """Overriding create_user func for ModUserManager."""

        # Agregar validaciones
        if not email:
            raise ValueError("You must provide an email...")

        # Ponemo en minuscula el dominio
        email = self.normalize_email(email)

        # Nos hizo el usuario en la variable 'user'
        user = self.model(
            email=email, user_name=user_name, first_name=first_name, **other_fields
        )

        # Seteamos password
        user.set_password(password)

        # Guardar en base de datos
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        """Overriding create_superuser func for ModUserManager."""

        # is_staff -> Verdadero
        # is_active -> Verdadero
        # is_superuser -> Verdadero
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_superuser", True)

        # Creamos el usuario con la funcion recien creada de create_user
        return self.create_user(email, user_name, first_name, password, **other_fields)

    # 2. create_superuser
    # admin -> 123456 -> createsuperuser
