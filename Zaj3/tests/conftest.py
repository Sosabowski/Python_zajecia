import pytest
import logging
from logger_config import setup_logging

logger = setup_logging()

def pytest_sessionstart(session):
    logger.info("Test session starts")

def pytest_sessionfinish(session, exitstatus):
    logger.info("Test session finishes")
    logger.info(f"Exit status: {exitstatus}")

def pytest_runtest_logreport(report):
    if report.when == 'call':
        if report.failed:
            logger.error(f"Test {report.nodeid} failed")
        elif report.skipped:
            logger.warning(f"Test {report.nodeid} skipped")
        else:
            logger.info(f"Test {report.nodeid} passed")