"""모델 테스트."""

import msgspec

from opendart_fss.models.base import BaseResponse
from opendart_fss.models.disclosure import (
    Company,
    CompanyResponse,
    Disclosure,
    DisclosureListResponse,
)
from opendart_fss.models.financial import FinancialAccount


class TestBaseModels:
    """기본 모델 테스트."""

    def test_base_response_decode(self) -> None:
        """BaseResponse 디코딩 테스트."""
        data = b'{"status": "000", "message": "\\uc815\\uc0c1"}'
        response = msgspec.json.decode(data, type=BaseResponse)
        assert response.status == "000"
        assert response.message == "정상"


class TestDisclosureModels:
    """공시정보 모델 테스트."""

    def test_disclosure_decode(self) -> None:
        """Disclosure 디코딩 테스트."""
        data = b"""{
            "corp_code": "00126380",
            "corp_name": "\\uc0bc\\uc131\\uc804\\uc790",
            "stock_code": "005930",
            "corp_cls": "Y",
            "report_nm": "\\uc0ac\\uc5c5\\ubcf4\\uace0\\uc11c",
            "rcept_no": "20240315000123",
            "flr_nm": "\\uc0bc\\uc131\\uc804\\uc790",
            "rcept_dt": "20240315",
            "rm": ""
        }"""
        disclosure = msgspec.json.decode(data, type=Disclosure)
        assert disclosure.corp_code == "00126380"
        assert disclosure.corp_name == "삼성전자"
        assert disclosure.stock_code == "005930"
        assert disclosure.corp_cls == "Y"

    def test_disclosure_list_response(self) -> None:
        """DisclosureListResponse 디코딩 테스트."""
        data = b"""{
            "status": "000",
            "message": "\\uc815\\uc0c1",
            "page_no": 1,
            "page_count": 10,
            "total_count": 1,
            "total_page": 1,
            "list": [{
                "corp_code": "00126380",
                "corp_name": "\\uc0bc\\uc131\\uc804\\uc790",
                "stock_code": "005930"
            }]
        }"""
        response = msgspec.json.decode(data, type=DisclosureListResponse)
        assert response.status == "000"
        assert len(response.items) == 1
        assert response.items[0].corp_code == "00126380"

    def test_company_response(self) -> None:
        """CompanyResponse 디코딩 테스트."""
        data = b"""{
            "status": "000",
            "message": "\\uc815\\uc0c1",
            "corp_code": "00126380",
            "corp_name": "\\uc0bc\\uc131\\uc804\\uc790",
            "corp_name_eng": "SAMSUNG ELECTRONICS CO., LTD.",
            "stock_name": "\\uc0bc\\uc131\\uc804\\uc790",
            "stock_code": "005930",
            "ceo_nm": "\\ud55c\\uc885\\ud76c",
            "corp_cls": "Y",
            "jurir_no": "1301110006246",
            "bizr_no": "1248100998",
            "adres": "\\uacbd\\uae30\\ub3c4 \\uc218\\uc6d0\\uc2dc",
            "hm_url": "www.samsung.com",
            "ir_url": "",
            "phn_no": "031-200-1114",
            "fax_no": "031-200-7538",
            "induty_code": "264",
            "est_dt": "19690113",
            "acc_mt": "12"
        }"""
        response = msgspec.json.decode(data, type=CompanyResponse)
        assert response.status == "000"
        assert response.corp_code == "00126380"
        assert response.corp_name == "삼성전자"
        assert response.ceo_nm == "한종희"

        company = response.to_company()
        assert isinstance(company, Company)
        assert company.corp_code == "00126380"


class TestFinancialModels:
    """재무정보 모델 테스트."""

    def test_financial_account_decode(self) -> None:
        """FinancialAccount 디코딩 테스트."""
        data = b"""{
            "rcept_no": "20240315000123",
            "reprt_code": "11011",
            "bsns_year": "2023",
            "corp_code": "00126380",
            "stock_code": "005930",
            "fs_div": "CFS",
            "fs_nm": "\\uc5f0\\uacb0\\uc7ac\\ubb34\\uc81c\\ud45c",
            "sj_div": "BS",
            "sj_nm": "\\uc7ac\\ubb34\\uc0c1\\ud0dc\\ud45c",
            "account_id": "ifrs-full_Assets",
            "account_nm": "\\uc790\\uc0b0\\ucd1d\\uacc4",
            "account_detail": "-",
            "thstrm_nm": "\\uc81c55\\uae30",
            "thstrm_amount": "455893816000000",
            "frmtrm_nm": "\\uc81c54\\uae30",
            "frmtrm_amount": "448423889000000",
            "ord": "1"
        }"""
        account = msgspec.json.decode(data, type=FinancialAccount)
        assert account.corp_code == "00126380"
        assert account.account_nm == "자산총계"
        assert account.thstrm_amount == "455893816000000"
        assert account.fs_div == "CFS"
