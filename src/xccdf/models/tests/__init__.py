import unittest

from xccdf.models.tests import test_element
from xccdf.models.tests import test_status
from xccdf.models.tests import test_title
from xccdf.models.tests import test_html_element
from xccdf.models.tests import test_description
from xccdf.models.tests import test_notice
from xccdf.models.tests import test_front_matter
from xccdf.models.tests import test_rear_matter
from xccdf.models.tests import test_platform
from xccdf.models.tests import test_version
from xccdf.models.tests import test_select
from xccdf.models.tests import test_profile
from xccdf.models.tests import test_tailoring
from xccdf.models.tests import test_ident
from xccdf.models.tests import test_rule
from xccdf.models.tests import test_group
from xccdf.models.tests import test_benchmark


def suite():
    suite = unittest.TestSuite()
    suite.addTests(test_element.suite())
    suite.addTests(test_status.suite())
    suite.addTests(test_title.suite())
    suite.addTests(test_html_element.suite())
    suite.addTests(test_description.suite())
    suite.addTests(test_notice.suite())
    suite.addTests(test_front_matter.suite())
    suite.addTests(test_rear_matter.suite())
    suite.addTests(test_platform.suite())
    suite.addTests(test_version.suite())
    suite.addTests(test_select.suite())
    suite.addTests(test_profile.suite())
    suite.addTests(test_tailoring.suite())
    suite.addTests(test_ident.suite())
    suite.addTests(test_rule.suite())
    suite.addTests(test_group.suite())
    suite.addTests(test_benchmark.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
