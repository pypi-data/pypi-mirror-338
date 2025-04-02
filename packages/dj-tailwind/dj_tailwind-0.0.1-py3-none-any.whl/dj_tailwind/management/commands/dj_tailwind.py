import os
import subprocess
import sys

import djclick as click
from django.conf import settings

dj_tailwind_app_name = settings.DJ_TAILWIND_APP_NAME  # type: ignore
dj_tailwind_django_app_name = "".join(
    word.capitalize() for word in settings.DJ_TAILWIND_APP_NAME.split("_")  # type: ignore
)


def run_npm_command(cwd, *args):
    try:
        subprocess.check_call(["npm", *args], cwd=cwd)
    except subprocess.CalledProcessError as err:
        raise click.ClickException(f"npm error: {err}")
    except FileNotFoundError as err:
        raise click.ClickException("npm is not installed or not found in PATH") from err
    except KeyboardInterrupt:
        pass


@click.group()
def dj_tailwind():
    """Run Tailwind-related commands."""


@dj_tailwind.command()
def init():
    """Initialize a Tailwind Django app."""
    try:
        from cookiecutter.main import cookiecutter  # pylint: disable=C0415
    except ImportError:
        click.echo("Installing cookiecutter with pip...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "cookiecutter"]
            )
            from cookiecutter.main import cookiecutter  # pylint: disable=C0415
        except Exception as e:
            raise click.ClickException(f"Failed to install cookiecutter: {e}")

    try:
        app_path = cookiecutter(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            output_dir=os.getcwd(),
            directory="cookiecutter",
            no_input=True,
            overwrite_if_exists=False,
            extra_context={
                "app_name": dj_tailwind_app_name,
                "django_app_name": dj_tailwind_django_app_name,
                "tailwind_root_source": settings.DJ_TAILWIND_ROOT_SOURCE,  # type: ignore
                "enable_daisyui": settings.DJ_TAILWIND_ENABLE_DAISYUI,  # type: ignore
            },
        )

        created_app = os.path.basename(app_path)
        click.secho(
            f"DJ Tailwind app '{created_app}' created.\n"
            f"Add '{created_app}' to INSTALLED_APPS, then run:\n"
            f"python manage.py dj_tailwind install",
            fg="green",
        )
    except Exception as err:
        raise click.ClickException(str(err))


@dj_tailwind.command()
def install():
    """Install NPM dependencies."""
    run_npm_command(dj_tailwind_app_name, "install")


@dj_tailwind.command()
def build():
    """Build Tailwind CSS."""
    run_npm_command(dj_tailwind_app_name, "run", "build")


@dj_tailwind.command()
def start():
    """Start watching Tailwind CSS sources for changes."""
    run_npm_command(dj_tailwind_app_name, "run", "dev")


@dj_tailwind.command()
def update():
    """Update NPM dependencies."""
    run_npm_command(dj_tailwind_app_name, "update")
