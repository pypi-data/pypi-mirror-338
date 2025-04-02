from django.apps import AppConfig


class DjTailwindConfig(AppConfig):
    name = "dj_tailwind"
    verbose_name = "Django Tailwind"

    def ready(self):
        # pylint: disable=import-outside-toplevel
        from django.conf import settings

        settings.DJ_TAILWIND_APP_NAME = getattr(
            settings, "DJ_TAILWIND_APP_NAME", "dj_tailwind_output"
        )
        settings.DJ_TAILWIND_CSS_OUTPUT = (
            f"{settings.DJ_TAILWIND_APP_NAME}/css/dist/tailwind.output.css"
        )
        settings.DJ_TAILWIND_ROOT_SOURCE = getattr(
            settings, "DJ_TAILWIND_ROOT_SOURCE", "../"
        )
        settings.DJ_TAILWIND_ENABLE_DAISYUI = getattr(
            settings, "DJ_TAILWIND_ENABLE_DAISYUI", False
        )
