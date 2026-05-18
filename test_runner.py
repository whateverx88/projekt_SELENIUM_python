import HtmlTestRunner
import unittest

loader = unittest.TestLoader()
suite = loader.discover('tests')

runner = HtmlTestRunner.HTMLTestRunner(
    output='test_reports',
    report_name='Test Report',
    report_title='Python/Selenium Automation Report',
    combine_reports = True
)

runner.run(suite)