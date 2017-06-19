from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
from unittest import TestCase


class Flake8Test(TestCase):

    def test_flake8(self):
        command = 'flake8 pybutton'
        try:
            subprocess.check_output(command.split())
        except subprocess.CalledProcessError as e:
            print('command: {}'.format(command))
            print(e.output)
            self.fail('flake8 failed with return code {}'.format(e.returncode))
