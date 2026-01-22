#!/usr/bin/env python3
"""
Workbook에서 문제 목록을 가져와 problems.json에 추가하는 스크립트

사용법:
    python fetch_problems.py 0x12              # 특정 챕터 fetch
    python fetch_problems.py 0x12 0x13         # 여러 챕터 fetch
    python fetch_problems.py --all             # 전체 챕터 다시 fetch
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
PROBLEMS_JSON = SCRIPT_DIR / "problems.json"

WORKBOOK_BASE_URL = "https://raw.githubusercontent.com/encrypted-def/basic-algo-lecture/master/workbook"

# 챕터 ID -> 디렉토리명 매핑 (디렉토리에서 자동 감지)
CHAPTER_NAMES = {
    "0x02": "기초 코드 작성 요령",
    "0x03": "배열",
    "0x04": "연결 리스트",
    "0x05": "스택",
    "0x06": "큐",
    "0x07": "덱",
    "0x08": "스택의 활용 (괄호 매칭)",
    "0x09": "BFS",
    "0x0a": "DFS",
    "0x0b": "재귀",
    "0x0c": "백트래킹",
    "0x0d": "시뮬레이션",
    "0x0e": "정렬 I",
    "0x0f": "정렬 II",
    "0x10": "다이나믹 프로그래밍",
    "0x11": "그리디",
    "0x12": "수학",
    "0x13": "이분탐색",
    "0x14": "투 포인터",
    "0x15": "해시",
    "0x16": "이진 검색 트리",
    "0x17": "우선순위 큐",
    "0x18": "그래프",
    "0x19": "트리",
    "0x1a": "위상 정렬",
    "0x1b": "최소 신장 트리",
    "0x1c": "플로이드 알고리즘",
    "0x1d": "다익스트라 알고리즘",
}


def find_chapter_dir(chapter_id: str) -> str | None:
    """로컬에서 챕터 디렉토리명 찾기"""
    pattern = re.compile(rf"^{chapter_id}\.\s*(.+)$", re.IGNORECASE)
    for item in ROOT_DIR.iterdir():
        if item.is_dir():
            match = pattern.match(item.name)
            if match:
                return item.name
    return None


def fetch_workbook(chapter_id: str) -> str | None:
    """GitHub에서 workbook 마크다운 가져오기"""
    # 0x09 -> 0x09.md (소문자 x 유지)
    formatted_id = "0x" + chapter_id[2:].upper()  # 0x0A, 0x0B 형식
    url = f"{WORKBOOK_BASE_URL}/{formatted_id}.md"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"[ERROR] {chapter_id}: workbook이 존재하지 않음 ({url})")
        else:
            print(f"[ERROR] {chapter_id}: HTTP 에러 {e.code}")
        return None
    except urllib.error.URLError as e:
        print(f"[ERROR] {chapter_id}: 네트워크 에러 - {e.reason}")
        return None


def parse_chapter_name(markdown: str) -> str | None:
    """마크다운 헤더에서 챕터명 추출"""
    # 첫 번째 # 헤더 찾기
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def parse_problems(markdown: str) -> list[dict]:
    """마크다운 테이블에서 문제 목록 추출"""
    problems = []

    # 테이블 행 패턴: | 분류 | 번호 | [제목](링크) | ... |
    # 예: | 연습 문제 | 1926 | [그림](https://...) | ... |
    pattern = re.compile(
        r"\|\s*(연습 문제|기본 문제✔?|응용 문제✔?)\s*\|\s*(\d+)\s*\|\s*\[([^\]]+)\]"
    )

    for match in pattern.finditer(markdown):
        category = match.group(1)
        number = int(match.group(2))
        name = match.group(3)

        problems.append({
            "number": number,
            "name": name,
            "category": category,
        })

    return problems


def load_problems_json() -> dict:
    """problems.json 로드 (없으면 빈 구조 반환)"""
    if PROBLEMS_JSON.exists():
        with open(PROBLEMS_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"chapters": {}}


def save_problems_json(data: dict) -> None:
    """problems.json 저장 (problems 배열은 한 줄씩)"""
    lines = ["{", '  "chapters": {']

    chapters = list(data["chapters"].items())
    for i, (chapter_id, chapter_data) in enumerate(chapters):
        lines.append(f'    "{chapter_id}": {{')
        lines.append(f'      "name": "{chapter_data["name"]}",')
        lines.append(f'      "dir": "{chapter_data["dir"]}",')
        lines.append('      "problems": [')

        problems = chapter_data["problems"]
        for j, p in enumerate(problems):
            comma = "," if j < len(problems) - 1 else ""
            row = f'{{"number": {p["number"]}, "name": "{p["name"]}", "category": "{p["category"]}"}}'
            lines.append(f"        {row}{comma}")

        lines.append("      ]")
        comma = "," if i < len(chapters) - 1 else ""
        lines.append(f"    }}{comma}")

    lines.append("  }")
    lines.append("}")
    lines.append("")

    with open(PROBLEMS_JSON, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def fetch_chapter(chapter_id: str, data: dict) -> bool:
    """
    단일 챕터 fetch
    Returns: 성공 여부
    """
    chapter_id = chapter_id.lower()

    # 1. workbook에서 문제 목록 가져오기
    markdown = fetch_workbook(chapter_id)
    if markdown is None:
        return False

    # 2. 문제 파싱
    problems = parse_problems(markdown)
    if not problems:
        print(f"[WARN] {chapter_id}: 문제를 찾을 수 없음")
        return False

    # 3. 디렉토리명 찾기 (로컬에서 또는 기본값 사용)
    dir_name = find_chapter_dir(chapter_id)
    if dir_name is None:
        # 디렉토리가 없으면 기본 이름으로 생성
        name = CHAPTER_NAMES.get(chapter_id, "Unknown")
        dir_name = f"{chapter_id}. {name}"
        print(f"[INFO] {chapter_id}: 디렉토리 없음, 기본값 사용 ({dir_name})")

    # 4. 챕터명 (workbook 헤더에서 추출, 없으면 CHAPTER_NAMES, 최후에 디렉토리에서)
    chapter_name = parse_chapter_name(markdown)
    if not chapter_name:
        chapter_name = CHAPTER_NAMES.get(chapter_id)
    if not chapter_name:
        match = re.match(r"^0x[0-9a-f]+\.\s*(.+)$", dir_name, re.IGNORECASE)
        chapter_name = match.group(1) if match else "Unknown"

    # 5. problems.json 업데이트
    data["chapters"][chapter_id] = {
        "name": chapter_name,
        "dir": dir_name,
        "problems": problems,
    }

    print(f"[OK] {chapter_id}: {len(problems)}개 문제 fetch 완료")
    return True


def main():
    parser = argparse.ArgumentParser(description="Workbook에서 문제 목록 fetch")
    parser.add_argument("chapters", nargs="*", help="fetch할 챕터 (예: 0x09)")
    parser.add_argument("--all", action="store_true", help="전체 챕터 다시 fetch")
    args = parser.parse_args()

    data = load_problems_json()

    if args.all:
        # 전체 다시 fetch (기존 챕터 목록 기준)
        chapters = list(data["chapters"].keys())
        if not chapters:
            print("[ERROR] problems.json에 챕터가 없음")
            sys.exit(1)
    elif args.chapters:
        chapters = args.chapters
    else:
        parser.print_help()
        sys.exit(1)

    success_count = 0
    for chapter_id in chapters:
        if fetch_chapter(chapter_id, data):
            success_count += 1

    if success_count > 0:
        # 챕터 ID 순으로 정렬
        sorted_chapters = dict(sorted(data["chapters"].items()))
        data["chapters"] = sorted_chapters
        save_problems_json(data)
        print(f"\n✅ {success_count}개 챕터 저장 완료")
    else:
        print("\n❌ 저장된 챕터 없음")
        sys.exit(1)


if __name__ == "__main__":
    main()
