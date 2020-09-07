#!/usr/bin/env python3

import os
import sys
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
    run_tests()
