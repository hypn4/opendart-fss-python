"""DS001 공시정보 모델."""

import msgspec

from opendart_fss.models.base import BaseResponse


class Disclosure(msgspec.Struct, kw_only=True):
    """공시 검색 결과."""

    corp_code: str  # 고유번호
    corp_name: str  # 회사명
    stock_code: str | None = None  # 종목코드
    corp_cls: str | None = None  # 법인구분 (Y/K/N/E)
    report_nm: str | None = None  # 보고서명
    rcept_no: str | None = None  # 접수번호
    flr_nm: str | None = None  # 공시제출인명
    rcept_dt: str | None = None  # 접수일자 (YYYYMMDD)
    rm: str | None = None  # 비고


class DisclosureListResponse(msgspec.Struct, kw_only=True):
    """공시 검색 응답."""

    status: str
    message: str
    page_no: int | None = None
    page_count: int | None = None
    total_count: int | None = None
    total_page: int | None = None
    items: list[Disclosure] = msgspec.field(default_factory=list, name="list")


class Company(msgspec.Struct, kw_only=True):
    """기업 개황 정보."""

    corp_code: str  # 고유번호
    corp_name: str  # 정식명칭
    corp_name_eng: str | None = None  # 영문명칭
    stock_name: str | None = None  # 종목명(상장사) 또는 약식명칭(기타법인)
    stock_code: str | None = None  # 상장회사인 경우 주식의 종목코드
    ceo_nm: str | None = None  # 대표자명
    corp_cls: str | None = None  # 법인구분 (Y/K/N/E)
    jurir_no: str | None = None  # 법인등록번호
    bizr_no: str | None = None  # 사업자등록번호
    adres: str | None = None  # 주소
    hm_url: str | None = None  # 홈페이지
    ir_url: str | None = None  # IR홈페이지
    phn_no: str | None = None  # 전화번호
    fax_no: str | None = None  # 팩스번호
    induty_code: str | None = None  # 업종코드
    est_dt: str | None = None  # 설립일 (YYYYMMDD)
    acc_mt: str | None = None  # 결산월 (MM)


class CompanyResponse(BaseResponse, kw_only=True):
    """기업 개황 응답."""

    corp_code: str  # 고유번호
    corp_name: str  # 정식명칭
    corp_name_eng: str | None = None  # 영문명칭
    stock_name: str | None = None  # 종목명(상장사) 또는 약식명칭(기타법인)
    stock_code: str | None = None  # 상장회사인 경우 주식의 종목코드
    ceo_nm: str | None = None  # 대표자명
    corp_cls: str | None = None  # 법인구분 (Y/K/N/E)
    jurir_no: str | None = None  # 법인등록번호
    bizr_no: str | None = None  # 사업자등록번호
    adres: str | None = None  # 주소
    hm_url: str | None = None  # 홈페이지
    ir_url: str | None = None  # IR홈페이지
    phn_no: str | None = None  # 전화번호
    fax_no: str | None = None  # 팩스번호
    induty_code: str | None = None  # 업종코드
    est_dt: str | None = None  # 설립일 (YYYYMMDD)
    acc_mt: str | None = None  # 결산월 (MM)

    def to_company(self) -> Company:
        """Company 객체로 변환."""
        return Company(
            corp_code=self.corp_code,
            corp_name=self.corp_name,
            corp_name_eng=self.corp_name_eng,
            stock_name=self.stock_name,
            stock_code=self.stock_code,
            ceo_nm=self.ceo_nm,
            corp_cls=self.corp_cls,
            jurir_no=self.jurir_no,
            bizr_no=self.bizr_no,
            adres=self.adres,
            hm_url=self.hm_url,
            ir_url=self.ir_url,
            phn_no=self.phn_no,
            fax_no=self.fax_no,
            induty_code=self.induty_code,
            est_dt=self.est_dt,
            acc_mt=self.acc_mt,
        )


class CorpCode(msgspec.Struct, kw_only=True):
    """고유번호 정보."""

    corp_code: str  # 고유번호
    corp_name: str  # 정식명칭
    stock_code: str | None = None  # 종목코드 (상장사만)
    modify_date: str | None = None  # 최종변경일 (YYYYMMDD)
