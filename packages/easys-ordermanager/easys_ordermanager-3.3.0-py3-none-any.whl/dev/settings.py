from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

SECRET_KEY = "m83&KC8Kby5He7D5Uq8BfBtz7om8bE3pp^L27tof^iaXB%d%3BG%dRoarF#6cRGY"
DEBUG = True

INSTALLED_APPS = [
    "dev.apps.DevConfig",
]

LANGUAGE_CODE = "en-us"
LANGUAGES = (
    ("de", "Deutsch"),
    ("en", "English"),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = "UTC"
