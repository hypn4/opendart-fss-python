"""OpenDART API 모델."""

from opendart_fss.models.base import BaseResponse
from opendart_fss.models.disclosure import (
    Company,
    CompanyResponse,
    CorpCode,
    Disclosure,
    DisclosureListResponse,
)
from opendart_fss.models.financial import (
    FinancialAccount,
    FinancialAccountListResponse,
    FinancialIndicator,
    FinancialIndicatorListResponse,
    XbrlTaxonomy,
    XbrlTaxonomyListResponse,
)
from opendart_fss.models.major_event import (
    BonusIssue,
    BonusIssueListResponse,
    CapitalChange,
    CapitalChangeListResponse,
    ConvertibleBond,
    ConvertibleBondListResponse,
    MergerDecision,
    MergerDecisionListResponse,
    SplitDecision,
    SplitDecisionListResponse,
)
from opendart_fss.models.registration import (
    DebtSecurities,
    DebtSecuritiesListResponse,
    EquitySecurities,
    EquitySecuritiesListResponse,
    MergerRegistration,
    MergerRegistrationListResponse,
    SplitRegistration,
    SplitRegistrationListResponse,
)
from opendart_fss.models.report import (
    DirectorCompensation,
    DirectorCompensationListResponse,
    DividendInfo,
    DividendInfoListResponse,
    Employee,
    EmployeeListResponse,
    Executive,
    ExecutiveListResponse,
    IndividualCompensation,
    IndividualCompensationListResponse,
    LargestShareholder,
    LargestShareholderListResponse,
    StockChange,
    StockChangeListResponse,
    TreasuryStock,
    TreasuryStockListResponse,
)
from opendart_fss.models.shareholder import (
    ExecutiveStock,
    ExecutiveStockListResponse,
    MajorStock,
    MajorStockListResponse,
)

__all__ = [
    # Base
    "BaseResponse",
    # Disclosure (DS001)
    "Disclosure",
    "DisclosureListResponse",
    "Company",
    "CompanyResponse",
    "CorpCode",
    # Report (DS002)
    "StockChange",
    "StockChangeListResponse",
    "DividendInfo",
    "DividendInfoListResponse",
    "TreasuryStock",
    "TreasuryStockListResponse",
    "LargestShareholder",
    "LargestShareholderListResponse",
    "Executive",
    "ExecutiveListResponse",
    "Employee",
    "EmployeeListResponse",
    "IndividualCompensation",
    "IndividualCompensationListResponse",
    "DirectorCompensation",
    "DirectorCompensationListResponse",
    # Financial (DS003)
    "FinancialAccount",
    "FinancialAccountListResponse",
    "FinancialIndicator",
    "FinancialIndicatorListResponse",
    "XbrlTaxonomy",
    "XbrlTaxonomyListResponse",
    # Shareholder (DS004)
    "MajorStock",
    "MajorStockListResponse",
    "ExecutiveStock",
    "ExecutiveStockListResponse",
    # Major Event (DS005)
    "CapitalChange",
    "CapitalChangeListResponse",
    "BonusIssue",
    "BonusIssueListResponse",
    "ConvertibleBond",
    "ConvertibleBondListResponse",
    "MergerDecision",
    "MergerDecisionListResponse",
    "SplitDecision",
    "SplitDecisionListResponse",
    # Registration (DS006)
    "EquitySecurities",
    "EquitySecuritiesListResponse",
    "DebtSecurities",
    "DebtSecuritiesListResponse",
    "MergerRegistration",
    "MergerRegistrationListResponse",
    "SplitRegistration",
    "SplitRegistrationListResponse",
]
