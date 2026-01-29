"""OpenDART API 클래스."""

from opendart_fss.api.base import BaseAPI
from opendart_fss.api.disclosure import DisclosureAPI
from opendart_fss.api.financial import FinancialAPI
from opendart_fss.api.major_event import MajorEventAPI
from opendart_fss.api.registration import RegistrationAPI
from opendart_fss.api.report import ReportAPI
from opendart_fss.api.shareholder import ShareholderAPI

__all__ = [
    "BaseAPI",
    "DisclosureAPI",
    "ReportAPI",
    "FinancialAPI",
    "ShareholderAPI",
    "MajorEventAPI",
    "RegistrationAPI",
]
