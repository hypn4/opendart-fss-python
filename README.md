# OpenDART FSS Python SDK

금융감독원 전자공시시스템 [OpenDART](https://opendart.fss.or.kr/) API를 위한 Python SDK입니다.

## 특징

- **Async only**: `httpx.AsyncClient` 기반의 비동기 API
- **타입 안전**: `msgspec`를 사용한 고성능 데이터 검증
- **전체 API 지원**: 6개 카테고리 83개 API 엔드포인트

## 설치

```bash
pip install opendart-fss
```

또는 uv 사용:

```bash
uv add opendart-fss
```

## 빠른 시작

### API 키 설정

OpenDART API 키는 두 가지 방법으로 설정할 수 있습니다:

**1. 환경변수 사용 (권장)**

```bash
# .env 파일 생성
cp .env.example .env
# .env 파일을 열고 API 키 입력
```

```python
# 환경변수가 설정되어 있으면 api_key 파라미터 생략 가능
async with OpenDartClient() as client:
    ...
```

**2. 직접 전달**

```python
async with OpenDartClient(api_key="YOUR_API_KEY") as client:
    ...
```

### 예제

```python
import asyncio
from opendart_fss import OpenDartClient

async def main():
    async with OpenDartClient() as client:  # 환경변수에서 API 키 로드
        # 공시 검색
        disclosures = await client.disclosure.search(
            corp_code="00126380",
            bgn_de="20240101",
            end_de="20241231"
        )

        for item in disclosures:
            print(f"{item.rcept_dt} - {item.report_nm}")

        # 기업 개황
        company = await client.disclosure.get_company("00126380")
        print(f"회사명: {company.corp_name}")
        print(f"대표자: {company.ceo_nm}")

        # 재무제표 조회
        financials = await client.financial.get_single_account(
            corp_code="00126380",
            bsns_year="2024",
            reprt_code="11011"  # 사업보고서
        )

        for item in financials:
            print(f"{item.account_nm}: {item.thstrm_amount}")

asyncio.run(main())
```

## API 카테고리

### DS001 공시정보 (4개)
- `client.disclosure.search()` - 공시검색
- `client.disclosure.get_company()` - 기업개황
- `client.disclosure.download_document()` - 공시서류 원본 다운로드
- `client.disclosure.download_corp_codes()` - 고유번호 전체 다운로드

### DS002 정기보고서 주요정보 (28개)
- `client.report.get_stock_changes()` - 증자(감자) 현황
- `client.report.get_dividends()` - 배당에 관한 사항
- `client.report.get_treasury_stock()` - 자기주식 취득/처분 현황
- `client.report.get_largest_shareholders()` - 최대주주 현황
- `client.report.get_largest_shareholder_changes()` - 최대주주 변동 현황
- `client.report.get_minority_shareholders()` - 소액주주 현황
- `client.report.get_executives()` - 임원 현황
- `client.report.get_employees()` - 직원 현황
- `client.report.get_individual_compensation()` - 개인별 보수 현황
- `client.report.get_director_compensation()` - 이사/감사 보수 현황
- `client.report.get_director_individual_compensation()` - 이사/감사 개인별 보수 현황
- `client.report.get_director_compensation_approval()` - 이사/감사 보수승인 현황
- `client.report.get_director_compensation_by_type()` - 유형별 이사/감사 보수 현황
- `client.report.get_unregistered_executive_compensation()` - 미등기임원 보수 현황
- `client.report.get_total_stock_quantity()` - 주식 총수 현황
- `client.report.get_debt_securities_issuance()` - 채무증권 발행실적
- `client.report.get_commercial_paper_balance()` - 기업어음증권 미상환 잔액
- `client.report.get_short_term_bond_balance()` - 단기사채 미상환 잔액
- `client.report.get_corporate_bond_balance()` - 회사채 미상환 잔액
- `client.report.get_hybrid_securities_balance()` - 신종자본증권 미상환 잔액
- `client.report.get_contingent_capital_balance()` - 조건부자본증권 미상환 잔액
- `client.report.get_auditor_opinion()` - 회계감사인 의견
- `client.report.get_audit_service_contract()` - 감사용역 계약 현황
- `client.report.get_non_audit_service_contract()` - 비감사용역 계약 현황
- `client.report.get_outside_directors()` - 사외이사 현황
- `client.report.get_other_corp_investments()` - 타법인 출자 현황
- `client.report.get_public_offering_fund_usage()` - 공모자금 사용 현황
- `client.report.get_private_placement_fund_usage()` - 사모자금 사용 현황

### DS003 정기보고서 재무정보 (6개)
- `client.financial.get_single_account()` - 단일회사 주요계정
- `client.financial.get_multi_account()` - 다중회사 주요계정
- `client.financial.get_full_statements()` - 전체 재무제표
- `client.financial.download_xbrl()` - XBRL 원본파일 다운로드
- `client.financial.get_xbrl_taxonomy()` - XBRL 택사노미
- `client.financial.get_single_indicators()` - 단일회사 재무지표

### DS004 지분공시 종합정보 (2개)
- `client.shareholder.get_major_stock()` - 대량보유 상황보고
- `client.shareholder.get_executive_stock()` - 임원/주요주주 소유보고

### DS005 주요사항보고서 (36개)
- `client.major_event.get_paid_capital_increase()` - 유상증자 결정
- `client.major_event.get_bonus_issue()` - 무상증자 결정
- `client.major_event.get_mixed_capital_increase()` - 유무상증자 결정
- `client.major_event.get_capital_reduction()` - 감자 결정
- `client.major_event.get_convertible_bond()` - 전환사채권 발행결정
- `client.major_event.get_bond_with_warrant()` - 신주인수권부사채권 발행결정
- `client.major_event.get_exchangeable_bond()` - 교환사채권 발행결정
- `client.major_event.get_write_off_contingent_capital()` - 상각형 조건부자본증권 발행결정
- `client.major_event.get_merger_decision()` - 합병 결정
- `client.major_event.get_split_decision()` - 분할 결정
- `client.major_event.get_split_merger_decision()` - 분할합병 결정
- `client.major_event.get_stock_exchange_decision()` - 주식 포괄적 교환·이전 결정
- `client.major_event.get_treasury_stock_acquisition()` - 자기주식 취득 결정
- `client.major_event.get_treasury_stock_disposal()` - 자기주식 처분 결정
- `client.major_event.get_treasury_trust_contract()` - 자기주식취득 신탁계약 체결 결정
- `client.major_event.get_treasury_trust_termination()` - 자기주식취득 신탁계약 해지 결정
- `client.major_event.get_business_acquisition()` - 영업양수 결정
- `client.major_event.get_business_disposal()` - 영업양도 결정
- `client.major_event.get_tangible_asset_acquisition()` - 유형자산 양수 결정
- `client.major_event.get_tangible_asset_disposal()` - 유형자산 양도 결정
- `client.major_event.get_other_corp_stock_acquisition()` - 타법인 주식 및 출자증권 양수 결정
- `client.major_event.get_other_corp_stock_disposal()` - 타법인 주식 및 출자증권 양도 결정
- `client.major_event.get_stock_related_bond_acquisition()` - 주권 관련 사채권 양수 결정
- `client.major_event.get_stock_related_bond_disposal()` - 주권 관련 사채권 양도 결정
- `client.major_event.get_asset_transfer()` - 영업양수도 등
- `client.major_event.get_default_occurrence()` - 채무불이행 등 발생
- `client.major_event.get_business_suspension()` - 영업정지 등
- `client.major_event.get_rehabilitation_filing()` - 회생절차 개시신청
- `client.major_event.get_dissolution_reason()` - 해산사유 발생
- `client.major_event.get_creditor_management_start()` - 채권자관리절차 개시신청
- `client.major_event.get_creditor_management_stop()` - 채권자관리절차 중단
- `client.major_event.get_litigation()` - 소송 등의 제기
- `client.major_event.get_overseas_listing_decision()` - 해외증권시장 주권등 상장결정
- `client.major_event.get_overseas_delisting_decision()` - 해외증권시장 주권등 상장폐지결정
- `client.major_event.get_overseas_listing()` - 해외증권시장 주권등 상장
- `client.major_event.get_overseas_delisting()` - 해외증권시장 주권등 상장폐지

### DS006 증권신고서 (6개)
- `client.registration.get_equity_securities()` - 지분증권 발행
- `client.registration.get_debt_securities()` - 채무증권 발행
- `client.registration.get_merger_registration()` - 합병 신고
- `client.registration.get_split_registration()` - 분할 신고
- `client.registration.get_depositary_receipt()` - 증권예탁증권
- `client.registration.get_stock_exchange_transfer()` - 주식의 포괄적 교환·이전

## 보고서 코드

| 코드 | 설명 |
|------|------|
| 11013 | 1분기보고서 |
| 11012 | 반기보고서 |
| 11014 | 3분기보고서 |
| 11011 | 사업보고서 |

```python
from opendart_fss import ReportCode

# 사업보고서 조회
financials = await client.financial.get_single_account(
    corp_code="00126380",
    bsns_year="2024",
    reprt_code=ReportCode.ANNUAL  # "11011"
)
```

## 에러 처리

```python
from opendart_fss import (
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ServerError,
)

try:
    company = await client.disclosure.get_company("invalid_code")
except AuthenticationError:
    print("API 키가 유효하지 않습니다")
except RateLimitError:
    print("요청 한도를 초과했습니다")
except ValidationError:
    print("잘못된 파라미터입니다")
except NotFoundError:
    print("데이터를 찾을 수 없습니다")
except ServerError:
    print("서버 오류가 발생했습니다")
```

## API 엔드포인트 검증

모든 API 엔드포인트가 정상 작동하는지 검증할 수 있습니다.

```bash
# 전체 엔드포인트 검증 (콘솔 출력)
uv run python scripts/verify_endpoints.py

# JSON 형식 출력
uv run python scripts/verify_endpoints.py --format json

# 마크다운 리포트 저장
uv run python scripts/verify_endpoints.py --format markdown -o report.md

# 특정 카테고리만 검증
uv run python scripts/verify_endpoints.py --category DS001

# 특정 엔드포인트만 검증
uv run python scripts/verify_endpoints.py --endpoint DS001-02
```

프로그래밍 방식으로도 사용할 수 있습니다:

```python
import asyncio
from opendart_fss.verification import EndpointVerifier, generate_report

async def main():
    async with EndpointVerifier() as verifier:
        results = await verifier.verify_all()
        report = generate_report(results, duration_seconds=0, format="console")
        print(report)

asyncio.run(main())
```

## 개발

```bash
# 의존성 설치
uv sync --group dev

# 테스트 실행
uv run pytest

# 통합 테스트 실행 (실제 API 호출)
uv run pytest tests/integration/ -v -m integration

# API 명세 스크래핑 (개발용)
uv run python scripts/scrape_api_specs.py
```

## 라이선스

MIT License
