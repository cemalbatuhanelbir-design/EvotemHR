import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def _extract_env_value(env_lines, key):
    for line in env_lines:
        if line.strip().startswith(f"{key}="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Expected '{key}' to be defined in .env.dist")


class EnvTemplateTests(unittest.TestCase):
    def setUp(self):
        env_path = BASE_DIR / ".env.dist"
        self.assertTrue(env_path.exists(), ".env.dist should be present for new deployments")
        self.env_lines = env_path.read_text().splitlines()

    def test_debug_is_disabled_by_default(self):
        self.assertEqual(_extract_env_value(self.env_lines, "DEBUG"), "False")

    def test_secret_key_is_placeholder_only(self):
        secret = _extract_env_value(self.env_lines, "SECRET_KEY")
        self.assertIn("change-me", secret.lower())
        self.assertNotIn("django-insecure", secret)

    def test_allowed_hosts_excludes_wildcard(self):
        allowed_hosts = _extract_env_value(self.env_lines, "ALLOWED_HOSTS")
        self.assertNotIn("*", allowed_hosts)
        self.assertGreater(len(allowed_hosts), 0)

    def test_csrf_trusted_origins_is_configurable(self):
        csrf_origins = _extract_env_value(self.env_lines, "CSRF_TRUSTED_ORIGINS")
        self.assertTrue(csrf_origins.startswith("http"))


class ReadmeGuidanceTests(unittest.TestCase):
    def setUp(self):
        self.readme_text = (BASE_DIR / "README.md").read_text()

    def test_readme_promotes_secure_defaults(self):
        self.assertIn("DEBUG=False", self.readme_text)
        self.assertIn("unique `SECRET_KEY`", self.readme_text)
        self.assertIn("ALLOWED_HOSTS", self.readme_text)

    def test_readme_includes_local_preview_steps(self):
        self.assertIn("runserver 0.0.0.0:8000", self.readme_text)
        self.assertIn("http://localhost:8000/", self.readme_text)
