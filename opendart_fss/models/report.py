"""DS002 정기보고서 주요정보 모델."""

import msgspec


class StockChange(msgspec.Struct, kw_only=True):
    """증자(감자) 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    isu_dcrs_de: str | None = None  # 주식발행(감소)일자
    isu_dcrs_stle: str | None = None  # 발행(감소)형태
    isu_dcrs_stock_knd: str | None = None  # 발행(감소)주식종류
    isu_dcrs_qy: str | None = None  # 발행(감소)수량
    isu_dcrs_mstvdv_fval_amount: str | None = None  # 발행(감소)주당액면가액
    isu_dcrs_mstvdv_amount: str | None = None  # 발행(감소)주당가액


class StockChangeListResponse(msgspec.Struct, kw_only=True):
    """증자(감자) 현황 응답."""

    status: str
    message: str
    items: list[StockChange] = msgspec.field(default_factory=list, name="list")


class DividendInfo(msgspec.Struct, kw_only=True):
    """배당에 관한 사항."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    se: str | None = None  # 구분
    stock_knd: str | None = None  # 주식종류
    thstrm: str | None = None  # 당기
    frmtrm: str | None = None  # 전기
    lwfr: str | None = None  # 전전기


class DividendInfoListResponse(msgspec.Struct, kw_only=True):
    """배당에 관한 사항 응답."""

    status: str
    message: str
    items: list[DividendInfo] = msgspec.field(default_factory=list, name="list")


class TreasuryStock(msgspec.Struct, kw_only=True):
    """자기주식 취득 및 처분 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    acqs_mth1: str | None = None  # 취득방법 대분류
    acqs_mth2: str | None = None  # 취득방법 중분류
    acqs_mth3: str | None = None  # 취득방법 소분류
    stock_knd: str | None = None  # 주식종류
    bsis_qy: str | None = None  # 기초수량
    change_qy_acqs: str | None = None  # 변동수량(취득)
    change_qy_dsps: str | None = None  # 변동수량(처분)
    change_qy_incnr: str | None = None  # 변동수량(소각)
    trmend_qy: str | None = None  # 기말수량
    rm: str | None = None  # 비고


class TreasuryStockListResponse(msgspec.Struct, kw_only=True):
    """자기주식 취득 및 처분 현황 응답."""

    status: str
    message: str
    items: list[TreasuryStock] = msgspec.field(default_factory=list, name="list")


class LargestShareholder(msgspec.Struct, kw_only=True):
    """최대주주 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    nm: str | None = None  # 성명
    relate: str | None = None  # 관계
    stock_knd: str | None = None  # 주식종류
    bsis_posesn_stock_co: str | None = None  # 기초소유주식수
    bsis_posesn_stock_qota_rt: str | None = None  # 기초소유주식지분율
    trmend_posesn_stock_co: str | None = None  # 기말소유주식수
    trmend_posesn_stock_qota_rt: str | None = None  # 기말소유주식지분율
    rm: str | None = None  # 비고


class LargestShareholderListResponse(msgspec.Struct, kw_only=True):
    """최대주주 현황 응답."""

    status: str
    message: str
    items: list[LargestShareholder] = msgspec.field(default_factory=list, name="list")


class Executive(msgspec.Struct, kw_only=True):
    """임원 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    nm: str | None = None  # 성명
    sexdstn: str | None = None  # 성별
    birth_ym: str | None = None  # 출생년월
    ofcps: str | None = None  # 직위
    rgbsn_od_yn: str | None = None  # 등기임원여부
    fte_yn: str | None = None  # 상근여부
    chrg_job: str | None = None  # 담당업무
    main_career: str | None = None  # 주요경력
    mxmm_shrholdr_relate: str | None = None  # 최대주주관계
    hffc_pd: str | None = None  # 재직기간
    tenure_end_on: str | None = None  # 임기만료일


class ExecutiveListResponse(msgspec.Struct, kw_only=True):
    """임원 현황 응답."""

    status: str
    message: str
    items: list[Executive] = msgspec.field(default_factory=list, name="list")


class Employee(msgspec.Struct, kw_only=True):
    """직원 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    fo_bbm: str | None = None  # 사업부문
    sexdstn: str | None = None  # 성별
    reform_bfe_emp_co_rgllbr: str | None = None  # 개정전직원수정규직
    reform_bfe_emp_co_cnttk: str | None = None  # 개정전직원수계약직
    reform_bfe_emp_co_etc: str | None = None  # 개정전직원수기타
    rgllbr_co: str | None = None  # 정규직수
    rgllbr_abacpt_labrr_co: str | None = None  # 정규직단시간근로자수
    cnttk_co: str | None = None  # 계약직수
    cnttk_abacpt_labrr_co: str | None = None  # 계약직단시간근로자수
    sm: str | None = None  # 합계
    avrg_cnwk_sdytrn: str | None = None  # 평균근속연수
    fyer_salary_totamt: str | None = None  # 연간급여총액
    jan_salary_am: str | None = None  # 1인평균급여액
    rm: str | None = None  # 비고


class EmployeeListResponse(msgspec.Struct, kw_only=True):
    """직원 현황 응답."""

    status: str
    message: str
    items: list[Employee] = msgspec.field(default_factory=list, name="list")


class IndividualCompensation(msgspec.Struct, kw_only=True):
    """개인별 보수 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    nm: str | None = None  # 이름
    ofcps: str | None = None  # 직위
    mendng_totamt: str | None = None  # 보수총액
    mendng_totamt_ct_incls_mendng: str | None = None  # 보수총액에포함된사항


class IndividualCompensationListResponse(msgspec.Struct, kw_only=True):
    """개인별 보수 현황 응답."""

    status: str
    message: str
    items: list[IndividualCompensation] = msgspec.field(
        default_factory=list, name="list"
    )


class DirectorCompensation(msgspec.Struct, kw_only=True):
    """이사/감사 보수 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    se: str | None = None  # 구분
    nmpr: str | None = None  # 인원수
    pymnt_totamt: str | None = None  # 보수총액
    psn1_avrg_pymnt_amt: str | None = None  # 1인당평균보수액
    rm: str | None = None  # 비고


class DirectorCompensationListResponse(msgspec.Struct, kw_only=True):
    """이사/감사 보수 현황 응답."""

    status: str
    message: str
    items: list[DirectorCompensation] = msgspec.field(default_factory=list, name="list")


class LargestShareholderChange(msgspec.Struct, kw_only=True):
    """최대주주 변동현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    change_on: str | None = None  # 변동일
    mxmm_shrholdr_nm: str | None = None  # 최대주주명
    posesn_stock_co: str | None = None  # 소유주식수
    qota_rt: str | None = None  # 지분율
    change_cause: str | None = None  # 변동원인
    rm: str | None = None  # 비고


class LargestShareholderChangeListResponse(msgspec.Struct, kw_only=True):
    """최대주주 변동현황 응답."""

    status: str
    message: str
    items: list[LargestShareholderChange] = msgspec.field(
        default_factory=list, name="list"
    )


class MinorityShareholder(msgspec.Struct, kw_only=True):
    """소액주주 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    se: str | None = None  # 구분
    shrholdr_co: str | None = None  # 주주수
    shrholdr_tot_co: str | None = None  # 전체주주수
    shrholdr_rate: str | None = None  # 주주비율
    hold_stock_co: str | None = None  # 보유주식수
    stock_tot_co: str | None = None  # 총발행주식수
    hold_stock_rate: str | None = None  # 보유주식비율


class MinorityShareholderListResponse(msgspec.Struct, kw_only=True):
    """소액주주 현황 응답."""

    status: str
    message: str
    items: list[MinorityShareholder] = msgspec.field(default_factory=list, name="list")


class DirectorIndividualCompensation(msgspec.Struct, kw_only=True):
    """이사·감사 개인별 보수현황 (5억원 이상)."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    nm: str | None = None  # 이름
    ofcps: str | None = None  # 직위
    mendng_totamt: str | None = None  # 보수총액
    mendng_totamt_ct_incls_mendng: str | None = None  # 보수총액비포함보수


class DirectorIndividualCompensationListResponse(msgspec.Struct, kw_only=True):
    """이사·감사 개인별 보수현황 응답."""

    status: str
    message: str
    items: list[DirectorIndividualCompensation] = msgspec.field(
        default_factory=list, name="list"
    )


class OtherCorpInvestment(msgspec.Struct, kw_only=True):
    """타법인 출자현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    inv_prm: str | None = None  # 법인명
    frst_acqs_de: str | None = None  # 최초취득일자
    invstmnt_purps: str | None = None  # 출자목적
    frst_acqs_amount: str | None = None  # 최초취득금액
    bsis_blce_qy: str | None = None  # 기초잔액수량
    bsis_blce_qota_rt: str | None = None  # 기초잔액지분율
    bsis_blce_acntbk_amount: str | None = None  # 기초잔액장부가액
    incrs_dcrs_acqs_dsps_qy: str | None = None  # 증감취득처분수량
    incrs_dcrs_acqs_dsps_amount: str | None = None  # 증감취득처분금액
    incrs_dcrs_evl_lstmn: str | None = None  # 증감평가손액
    trmend_blce_qy: str | None = None  # 기말잔액수량
    trmend_blce_qota_rt: str | None = None  # 기말잔액지분율
    trmend_blce_acntbk_amount: str | None = None  # 기말잔액장부가액
    recent_bsns_year_fnnr_sttus_tot_assets: str | None = None  # 최근사업연도총자산
    recent_bsns_year_fnnr_sttus_thstrm_ntpf: str | None = None  # 최근사업연도당기순이익


class OtherCorpInvestmentListResponse(msgspec.Struct, kw_only=True):
    """타법인 출자현황 응답."""

    status: str
    message: str
    items: list[OtherCorpInvestment] = msgspec.field(default_factory=list, name="list")


class TotalStockQuantity(msgspec.Struct, kw_only=True):
    """주식의 총수 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    se: str | None = None  # 구분
    isu_stock_totqy: str | None = None  # 발행할주식의총수
    now_to_isu_stock_totqy: str | None = None  # 현재까지발행한주식의총수
    now_to_dcrs_stock_totqy: str | None = None  # 현재까지감소한주식의총수
    redc: str | None = None  # 감자
    profit_incnr: str | None = None  # 이익소각
    rdmstk_repy: str | None = None  # 상환주식의상환
    etc: str | None = None  # 기타
    istc_totqy: str | None = None  # 발행주식의총수
    tesstk_co: str | None = None  # 자기주식수
    distb_stock_co: str | None = None  # 유통주식수


class TotalStockQuantityListResponse(msgspec.Struct, kw_only=True):
    """주식의 총수 현황 응답."""

    status: str
    message: str
    items: list[TotalStockQuantity] = msgspec.field(default_factory=list, name="list")


class DebtSecuritiesIssuance(msgspec.Struct, kw_only=True):
    """채무증권 발행실적."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    isu_cmpny: str | None = None  # 발행회사
    scrits_knd_nm: str | None = None  # 증권종류
    isu_mth_nm: str | None = None  # 발행방법
    isu_de: str | None = None  # 발행일자
    facvalu_totamt: str | None = None  # 권면총액
    intrt: str | None = None  # 이자율
    evl_grad_instt: str | None = None  # 평가등급(평가기관)
    mtd: str | None = None  # 만기일
    repy_at: str | None = None  # 상환여부
    mngt_cmpny: str | None = None  # 주관회사


class DebtSecuritiesIssuanceListResponse(msgspec.Struct, kw_only=True):
    """채무증권 발행실적 응답."""

    status: str
    message: str
    items: list[DebtSecuritiesIssuance] = msgspec.field(
        default_factory=list, name="list"
    )


class CommercialPaperBalance(msgspec.Struct, kw_only=True):
    """기업어음증권 미상환 잔액."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    sm: str | None = None  # 합계


class CommercialPaperBalanceListResponse(msgspec.Struct, kw_only=True):
    """기업어음증권 미상환 잔액 응답."""

    status: str
    message: str
    items: list[CommercialPaperBalance] = msgspec.field(
        default_factory=list, name="list"
    )


class ShortTermBondBalance(msgspec.Struct, kw_only=True):
    """단기사채 미상환 잔액."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    sm: str | None = None  # 합계
    isu_lmt: str | None = None  # 발행한도
    remndr_lmt: str | None = None  # 잔여한도


class ShortTermBondBalanceListResponse(msgspec.Struct, kw_only=True):
    """단기사채 미상환 잔액 응답."""

    status: str
    message: str
    items: list[ShortTermBondBalance] = msgspec.field(default_factory=list, name="list")


class CorporateBondBalance(msgspec.Struct, kw_only=True):
    """회사채 미상환 잔액."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    remndr_exprtn1: str | None = None  # 잔여만기1년이하
    remndr_exprtn2: str | None = None  # 잔여만기1년초과2년이하
    remndr_exprtn3: str | None = None  # 잔여만기2년초과3년이하
    remndr_exprtn4: str | None = None  # 잔여만기3년초과4년이하
    remndr_exprtn5: str | None = None  # 잔여만기4년초과5년이하
    remndr_exprtn_etc: str | None = None  # 잔여만기5년초과
    sm: str | None = None  # 합계


class CorporateBondBalanceListResponse(msgspec.Struct, kw_only=True):
    """회사채 미상환 잔액 응답."""

    status: str
    message: str
    items: list[CorporateBondBalance] = msgspec.field(default_factory=list, name="list")


class HybridSecuritiesBalance(msgspec.Struct, kw_only=True):
    """신종자본증권 미상환 잔액."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    remndr_exprtn1: str | None = None  # 잔여만기1년이하
    remndr_exprtn2: str | None = None  # 잔여만기1년초과5년이하
    remndr_exprtn3: str | None = None  # 잔여만기5년초과10년이하
    remndr_exprtn4: str | None = None  # 잔여만기10년초과15년이하
    remndr_exprtn5: str | None = None  # 잔여만기15년초과20년이하
    remndr_exprtn_etc: str | None = None  # 잔여만기20년초과30년이하
    sm: str | None = None  # 합계


class HybridSecuritiesBalanceListResponse(msgspec.Struct, kw_only=True):
    """신종자본증권 미상환 잔액 응답."""

    status: str
    message: str
    items: list[HybridSecuritiesBalance] = msgspec.field(
        default_factory=list, name="list"
    )


class ContingentCapitalBalance(msgspec.Struct, kw_only=True):
    """조건부자본증권 미상환 잔액."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    remndr_exprtn1: str | None = None  # 잔여만기1년이하
    remndr_exprtn2: str | None = None  # 잔여만기1년초과2년이하
    remndr_exprtn3: str | None = None  # 잔여만기2년초과3년이하
    remndr_exprtn4: str | None = None  # 잔여만기3년초과4년이하
    remndr_exprtn5: str | None = None  # 잔여만기4년초과5년이하
    remndr_exprtn_etc: str | None = None  # 잔여만기5년초과
    sm: str | None = None  # 합계


class ContingentCapitalBalanceListResponse(msgspec.Struct, kw_only=True):
    """조건부자본증권 미상환 잔액 응답."""

    status: str
    message: str
    items: list[ContingentCapitalBalance] = msgspec.field(
        default_factory=list, name="list"
    )


class AuditorOpinion(msgspec.Struct, kw_only=True):
    """회계감사인의 명칭 및 감사의견."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bsns_year: str | None = None  # 사업연도
    adtor: str | None = None  # 감사인
    adt_reprt_opnn_ctt: str | None = None  # 감사보고서의견내용
    adt_reprt_opnn: str | None = None  # 감사보고서의견
    emphs_mtr_ctt: str | None = None  # 강조사항내용
    core_adt_mtr_ctt: str | None = None  # 핵심감사사항내용


class AuditorOpinionListResponse(msgspec.Struct, kw_only=True):
    """회계감사인의 명칭 및 감사의견 응답."""

    status: str
    message: str
    items: list[AuditorOpinion] = msgspec.field(default_factory=list, name="list")


class AuditServiceContract(msgspec.Struct, kw_only=True):
    """감사용역 체결현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bsns_year: str | None = None  # 사업연도
    adtor: str | None = None  # 감사인
    cn_rs: str | None = None  # 계약내용보수
    cn_tm: str | None = None  # 계약내용시간
    real_cn_rs: str | None = None  # 실제수행내용보수
    real_cn_tm: str | None = None  # 실제수행내용시간


class AuditServiceContractListResponse(msgspec.Struct, kw_only=True):
    """감사용역 체결현황 응답."""

    status: str
    message: str
    items: list[AuditServiceContract] = msgspec.field(default_factory=list, name="list")


class NonAuditServiceContract(msgspec.Struct, kw_only=True):
    """회계감사인과의 비감사용역 계약체결 현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bsns_year: str | None = None  # 사업연도
    svc_ctt: str | None = None  # 용역내용
    svc_cn_rs: str | None = None  # 용역계약보수
    rm: str | None = None  # 비고


class NonAuditServiceContractListResponse(msgspec.Struct, kw_only=True):
    """회계감사인과의 비감사용역 계약체결 현황 응답."""

    status: str
    message: str
    items: list[NonAuditServiceContract] = msgspec.field(
        default_factory=list, name="list"
    )


class OutsideDirector(msgspec.Struct, kw_only=True):
    """사외이사 및 그 변동현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bsis_at_od_drctr_co: str | None = None  # 기초사외이사수
    dirctn_chg_od_drctr_co: str | None = None  # 변동현황선임
    rsigntn_od_drctr_co: str | None = None  # 변동현황사임
    trmend_at_od_drctr_co: str | None = None  # 기말사외이사수
    rm: str | None = None  # 비고


class OutsideDirectorListResponse(msgspec.Struct, kw_only=True):
    """사외이사 및 그 변동현황 응답."""

    status: str
    message: str
    items: list[OutsideDirector] = msgspec.field(default_factory=list, name="list")


class UnregisteredExecutiveCompensation(msgspec.Struct, kw_only=True):
    """미등기임원 보수현황."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    nmpr: str | None = None  # 인원수
    pymnt_totamt: str | None = None  # 보수총액
    psn1_avrg_pymnt_amt: str | None = None  # 1인당평균보수액
    rm: str | None = None  # 비고


class UnregisteredExecutiveCompensationListResponse(msgspec.Struct, kw_only=True):
    """미등기임원 보수현황 응답."""

    status: str
    message: str
    items: list[UnregisteredExecutiveCompensation] = msgspec.field(
        default_factory=list, name="list"
    )


class DirectorCompensationApproval(msgspec.Struct, kw_only=True):
    """이사·감사 보수현황 (주주총회 승인금액)."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    se: str | None = None  # 구분
    gmtsck_confm_amount: str | None = None  # 주주총회승인금액
    py_amount: str | None = None  # 지급액


class DirectorCompensationApprovalListResponse(msgspec.Struct, kw_only=True):
    """이사·감사 보수현황 (주주총회 승인금액) 응답."""

    status: str
    message: str
    items: list[DirectorCompensationApproval] = msgspec.field(
        default_factory=list, name="list"
    )


class DirectorCompensationByType(msgspec.Struct, kw_only=True):
    """이사·감사 보수현황 (유형별)."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    se: str | None = None  # 구분
    nmpr: str | None = None  # 인원수
    pymnt_totamt: str | None = None  # 보수총액
    psn1_avrg_pymnt_amt: str | None = None  # 1인당평균보수액
    rm: str | None = None  # 비고


class DirectorCompensationByTypeListResponse(msgspec.Struct, kw_only=True):
    """이사·감사 보수현황 (유형별) 응답."""

    status: str
    message: str
    items: list[DirectorCompensationByType] = msgspec.field(
        default_factory=list, name="list"
    )


class PublicOfferingFundUsage(msgspec.Struct, kw_only=True):
    """공모자금의 사용내역."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    pssrp_cptal_use_dtls_rcppln: str | None = None  # 납입일
    pssrp_cptal_use_dtls_use_pps: str | None = None  # 자금사용목적
    pssrp_cptal_use_dtls_pssrp_cptal: str | None = None  # 공모자금
    pssrp_cptal_use_dtls_real_use_amount: str | None = None  # 실제사용금액
    pssrp_cptal_use_dtls_dfra: str | None = None  # 차액
    pssrp_cptal_use_dtls_csr: str | None = None  # 차이사유


class PublicOfferingFundUsageListResponse(msgspec.Struct, kw_only=True):
    """공모자금의 사용내역 응답."""

    status: str
    message: str
    items: list[PublicOfferingFundUsage] = msgspec.field(
        default_factory=list, name="list"
    )


class PrivatePlacementFundUsage(msgspec.Struct, kw_only=True):
    """사모자금의 사용내역."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    prfd_cptal_use_dtls_rcppln: str | None = None  # 납입일
    prfd_cptal_use_dtls_use_pps: str | None = None  # 자금사용목적
    prfd_cptal_use_dtls_prfd_cptal: str | None = None  # 사모자금
    prfd_cptal_use_dtls_real_use_amount: str | None = None  # 실제사용금액
    prfd_cptal_use_dtls_dfra: str | None = None  # 차액
    prfd_cptal_use_dtls_csr: str | None = None  # 차이사유


class PrivatePlacementFundUsageListResponse(msgspec.Struct, kw_only=True):
    """사모자금의 사용내역 응답."""

    status: str
    message: str
    items: list[PrivatePlacementFundUsage] = msgspec.field(
        default_factory=list, name="list"
    )
