import unittest
import sys
from multiprocessing import freeze_support
from tests import suites as test_suites
import logging


def run_tests():
    freeze_support()
    logging.disable(logging.CRITICAL)
    ret = True
    print('Testing Workflows:')
    ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.workflow_suite).wasSuccessful()
    print('\nTesting Execution:')
    ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.execution_suite).wasSuccessful()
    print('\nTesting Cases:')
    ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.case_suite).wasSuccessful()
    print('\nTesting Server:')
    ret &= unittest.TextTestRunner(verbosity=1).run(test_suites.server_suite).wasSuccessful()
    return ret


if __name__ == '__main__':
    try:
        successful = not run_tests()
        sys.exit(successful)
    except KeyboardInterrupt:
        print('\nInterrupted! Ending full test')
