from django.test import TestCase, Client
from django.conf import settings
import os


class DefaultProjectStructureTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_installed_apps_defaults(self):
        """Apps por defecto deben estar en INSTALLED_APPS"""
        default_apps = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
        ]
        for app in default_apps:
            self.assertIn(app, settings.INSTALLED_APPS)

    def test_middleware_defaults(self):
        """Middleware por defecto deben estar configurados"""
        default_middleware = [
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ]
        for mw in default_middleware:
            self.assertIn(mw, settings.MIDDLEWARE)

    def test_admin_url_accessible(self):
        """/admin/ debe estar disponible (aunque redireccione sin login)"""
        response = self.client.get("/admin/")
        self.assertIn(response.status_code, [200, 302])

    def test_root_url_defined(self):
        """/ debe devolver 200, 302 o 404 si no hay vista definida"""
        response = self.client.get("/")
        self.assertIn(response.status_code, [200, 302, 404])

    def test_database_engine_supported(self):
        """Verifica que se use PostgreSQL o SQLite"""
        engine = settings.DATABASES["default"]["ENGINE"]
        self.assertIn(
            engine, ["django.db.backends.sqlite3", "django.db.backends.postgresql"]
        )

    def test_debug_defined(self):
        """Solo verifica que DEBUG esté definido (no asume True/False)"""
        self.assertIsInstance(settings.DEBUG, bool)

    def test_staticfiles_configured(self):
        """Debe haber configuración STATIC_URL"""
        self.assertTrue(hasattr(settings, "STATIC_URL"))
        self.assertTrue(settings.STATIC_URL.startswith("/"))

    def test_manage_py_likely_exists(self):
        """Verifica manage.py relativo al entorno Docker"""
        from pathlib import Path

        base = Path(__file__).resolve()
        for parent in base.parents:
            if (parent / "manage.py").is_file():
                self.assertTrue(True)
                return
        self.fail("manage.py no encontrado en los padres del archivo actual")
