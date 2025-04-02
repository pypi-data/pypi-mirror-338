from django.apps import AppConfig


class {{ cookiecutter.django_app_name }}Config(AppConfig):
    name = '{{ cookiecutter.app_name }}'
    description = 'Django app for managing Tailwind CSS'
