from abc import ABC, abstractmethod
import os
import requests
from dotenv import load_dotenv
from logging import getLogger
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = getLogger(__name__)


# Define the Strategy interface
class ReportStrategy(ABC):
    @abstractmethod
    def info(self, content: str):
        pass

    def event(self, content: str):
        pass

    def warning(self, content: str):
        pass

    def error(self, content: str):
        pass


class LogReportStrategy(ReportStrategy):
    def info(self, content: str):
        logger.info(content)

    def event(self, content: str):
        logger.info(content)

    def warning(self, content: str):
        logger.warning(content)

    def error(self, content: str):
        logger.error(content)


class DiscordReportStrategy(ReportStrategy):
    def __init__(self):
        load_dotenv()
        self.info_url = os.getenv("REPORT_INFO_WEBHOOK")
        self.event_url = os.getenv("REPORT_EVENT_WEBHOOK")
        self.warning_url = os.getenv("REPORT_WARNING_WEBHOOK")
        self.error_url = os.getenv("REPORT_ERROR_WEBHOOK")
        self.username = os.getenv("DiscorfReportStrategy")

        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504], allowed_methods=["POST"])
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def send_message(self, url: str, content: str):
        data = {"content": content, "username": self.username}
        result = self.session.post(url, json=data, timeout=10)
        if result.status_code not in (200, 204):
            logger.error(
                f"Error sending message to {url}, status_code: {result.status_code}, text: {result.text}, content: {content}"
            )
        return result

    def info(self, content: str):
        self.send_message(self.info_url, content=content)

    def event(self, content: str):
        self.send_message(self.event_url, content=content)

    def warning(self, content: str):
        self.send_message(self.warning_url, content=content)

    def error(self, content: str):
        self.send_message(self.error_url, content=content)
