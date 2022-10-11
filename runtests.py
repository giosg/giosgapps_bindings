#!/usr/bin/env python3

import os
import sys
import subprocess
APP_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, APP_DIR)
SETTINGS_DICT = {
    'INSTALLED_APPS': ('giosgapps_bindings',),
    'ROOT_URLCONF': 'giosgapps_bindings.tests.urls',
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        },
    }
}


def run_linter():
    try:
        subprocess.check_output(['flake8', '.']).decode('utf-8')
        print("Linter did not spot problems 👌")
        return True
    except subprocess.CalledProcessError as cpe:
        out = cpe.output.decode("utf-8")
        print(f"Linter error. Return code {cpe.returncode}. Error: {out}")
        exit(cpe.returncode)


def run_tests():
    from django.conf import settings
    settings.configure(**SETTINGS_DICT)

    import django
    django.setup()

    from django.test.utils import get_runner
    TestRunner = get_runner(settings)

    test_runner = TestRunner(verbosity=2, interactive=True)
    failures = test_runner.run_tests(['giosgapps_bindings.tests'])
    sys.exit(failures)


if __name__ == '__main__':
    run_linter()
    run_tests()
