#!/usr/bin/env python3
"""OpenDART API 명세 스크래핑 스크립트.

crawl4ai를 사용하여 OpenDART 개발가이드에서 API 명세를 추출합니다.
"""

import asyncio
import json
import re
from pathlib import Path

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

GUIDE_BASE_URL = "https://opendart.fss.or.kr/guide"

API_GROUPS = {
    "DS001": "disclosure",  # 공시정보
    "DS002": "report",  # 정기보고서 주요정보
    "DS003": "financial",  # 정기보고서 재무정보
    "DS004": "shareholder",  # 지분공시 종합정보
    "DS005": "major_event",  # 주요사항보고서
    "DS006": "registration",  # 증권신고서
}


def parse_api_list_from_html(html: str, group_code: str) -> list[dict]:
    """HTML에서 API 목록을 파싱합니다."""
    apis = []

    # Find API names from table rows
    # Pattern: <td>번호</td><td>API명</td><td>설명</td><td><a href="...">바로가기</a></td>
    row_pattern = r'<tr>\s*<td>(\d+)</td>\s*<td>([^<]+)</td>\s*<td[^>]*>([^<]+)</td>\s*<td><a href="([^"]+)"'
    row_matches = re.findall(row_pattern, html, re.DOTALL)

    for num, name, desc, link in row_matches:
        api_id_match = re.search(r"apiId=(\d+)", link)
        if api_id_match:
            apis.append(
                {
                    "api_id": api_id_match.group(1),
                    "api_name": name.strip(),
                    "description": desc.strip(),
                    "detail_url": f"{GUIDE_BASE_URL}/detail.do?apiGrpCd={group_code}&apiId={api_id_match.group(1)}",
                }
            )

    return apis


def parse_api_detail_from_html(html: str, api_info: dict) -> dict:
    """HTML에서 API 상세 정보를 파싱합니다."""
    result = {
        "api_id": api_info["api_id"],
        "api_name": api_info["api_name"],
        "description": api_info.get("description", ""),
        "endpoints": [],
        "request_params": [],
        "response_fields": [],
    }

    # Parse endpoints (JSON and XML URLs)
    # Pattern: <td>GET</td><td class="tl">URL</td><td>UTF-8</td><td>JSON/XML</td>
    endpoint_pattern = (
        r"<td>GET</td>\s*<td[^>]*>([^<]+)</td>\s*<td>UTF-8</td>\s*<td>(JSON|XML)</td>"
    )
    endpoint_matches = re.findall(endpoint_pattern, html)
    for url, format_type in endpoint_matches:
        result["endpoints"].append(
            {
                "url": url.strip(),
                "format": format_type,
            }
        )

    # Parse request parameters
    # Each parameter is in a <tr> with 5 <td> elements
    # Pattern matches: <tr><td class="tl">name</td><td class="tl">label</td><td>type</td><td>Y/N</td><td class="tl">desc</td></tr>
    param_pattern = r'<tr>\s*<td class="tl">([a-z_]+)</td>\s*<td class="tl">([^<]+)</td>\s*<td>([^<]+)</td>\s*<td>([YN])</td>\s*<td class="tl">(.*?)</td>\s*</tr>'
    param_matches = re.findall(param_pattern, html, re.DOTALL)

    for param_name, label, param_type, required, desc in param_matches:
        # Clean description (remove HTML tags)
        clean_desc = re.sub(r"<[^>]+>", " ", desc).strip()
        clean_desc = re.sub(r"\s+", " ", clean_desc)
        result["request_params"].append(
            {
                "name": param_name.strip(),
                "label": label.strip(),
                "type": param_type.strip(),
                "required": required == "Y",
                "description": clean_desc,
            }
        )

    # Parse response fields
    # Look for iconFile markers: <i class="iconFile"></i>field_name
    response_pattern = r'<i class="iconFile"></i>([a-z_]+)\s*</td>\s*<td class="tl">([^<]+)</td>\s*<td class="tl">([^<]*)'
    response_matches = re.findall(response_pattern, html)

    for field_name, label, desc in response_matches:
        result["response_fields"].append(
            {
                "name": field_name.strip(),
                "label": label.strip(),
                "description": desc.strip(),
            }
        )

    return result


async def scrape_api_list(crawler: AsyncWebCrawler, group_code: str) -> list[dict]:
    """API 그룹의 API 목록을 스크래핑합니다."""
    url = f"{GUIDE_BASE_URL}/main.do?apiGrpCd={group_code}"

    config = CrawlerRunConfig()
    result = await crawler.arun(url=url, config=config)

    if not result.success or not result.html:
        print(f"Failed to scrape API list for {group_code}")
        return []

    return parse_api_list_from_html(result.html, group_code)


async def scrape_api_detail(crawler: AsyncWebCrawler, api_info: dict) -> dict | None:
    """API 상세 정보를 스크래핑합니다."""
    url = api_info["detail_url"]

    config = CrawlerRunConfig()
    result = await crawler.arun(url=url, config=config)

    if not result.success or not result.html:
        print(f"  Failed to scrape: {api_info['api_name']}")
        return None

    return parse_api_detail_from_html(result.html, api_info)


async def scrape_all_apis() -> dict[str, list[dict]]:
    """모든 API 그룹의 명세를 스크래핑합니다."""
    browser_config = BrowserConfig(headless=True)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        all_specs: dict[str, list[dict]] = {}

        for group_code, group_name in API_GROUPS.items():
            print(f"Scraping {group_code} ({group_name})...")

            api_list = await scrape_api_list(crawler, group_code)
            print(f"  Found {len(api_list)} APIs")

            specs = []
            for api_info in api_list:
                detail = await scrape_api_detail(crawler, api_info)
                if detail:
                    detail["group_code"] = group_code
                    detail["group_name"] = group_name
                    specs.append(detail)
                    print(
                        f"    - {detail['api_name']}: {len(detail['request_params'])} params, {len(detail['response_fields'])} fields"
                    )

            all_specs[group_name] = specs

        return all_specs


def save_specs(specs: dict[str, list[dict]], output_dir: Path) -> None:
    """스크래핑한 명세를 JSON 파일로 저장합니다."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for group_name, api_specs in specs.items():
        output_file = output_dir / f"{group_name}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(api_specs, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(api_specs)} APIs to {output_file}")

    # 전체 명세도 저장
    all_specs_file = output_dir / "all_apis.json"
    with open(all_specs_file, "w", encoding="utf-8") as f:
        json.dump(specs, f, ensure_ascii=False, indent=2)
    print(f"Saved all specs to {all_specs_file}")


async def main() -> None:
    """메인 함수."""
    print("OpenDART API 명세 스크래핑 시작...")

    specs = await scrape_all_apis()

    # 결과 저장
    output_dir = Path(__file__).parent.parent / "specs"
    save_specs(specs, output_dir)

    # 통계 출력
    total_apis = sum(len(apis) for apis in specs.values())
    print(f"\n총 {total_apis}개 API 명세 스크래핑 완료")


if __name__ == "__main__":
    asyncio.run(main())
