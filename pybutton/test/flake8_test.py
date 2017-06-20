from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
import sys
from unittest import TestCase


class Flake8Test(TestCase):

    def test_flake8(self):

        # As of v3, flake8 is no longer supports python 2.6
        if sys.version_info[0] == 2 and sys.version_info[1] < 7:
            return

        command = 'flake8 pybutton'
        p = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        stdout, _ = p.communicate()

        if p.returncode != 0:
            print(stdout)
            self.fail(
                'flake8 failed with return code {0}'.format(p.returncode)
            )
