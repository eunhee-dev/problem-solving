#!/usr/bin/env python3
"""
README 자동 생성/업데이트 스크립트

사용법:
    python generate_readme.py              # 전체 업데이트
    python generate_readme.py 0x09         # 특정 챕터만
    python generate_readme.py --check      # 변경 필요 여부만 확인
"""

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
PROBLEMS_JSON = SCRIPT_DIR / "problems.json"

README_TEMPLATE = """# {chapter_id}. {chapter_name}

## 개요

-

## 문제 풀이 현황

{problem_table}

<details>
<summary>힌트 보기</summary>

{hints}
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

-

</details>
"""


def load_problems() -> dict:
    """problems.json 로드"""
    with open(PROBLEMS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def find_solved_problems(chapter_dir: Path) -> dict[int, tuple[str, str]]:
    """
    챕터 디렉토리에서 풀이 완료된 문제 찾기
    Returns: {문제번호: (디렉토리명, 문제명)}
    """
    solved = {}
    if not chapter_dir.exists():
        return solved

    # 패턴: "12345번. 문제명" 또는 "12345번.문제명"
    pattern = re.compile(r"^(\d+)번[.\s]*(.*)$")

    for item in chapter_dir.iterdir():
        if item.is_dir():
            match = pattern.match(item.name)
            if match:
                problem_num = int(match.group(1))
                problem_name = match.group(2).strip() or f"문제 {problem_num}"
                solved[problem_num] = (item.name, problem_name)

    return solved


def generate_table_row(number: int, name: str, category: str, solved_dir: str | None) -> str:
    """문제 테이블 행 생성"""
    problem_link = f"[{name}](https://www.acmicpc.net/problem/{number})"

    if solved_dir:
        # 공백만 %20으로 인코딩, 한글은 유지
        encoded_dir = solved_dir.replace(" ", "%20")
        solution_link = f"[코드](./{encoded_dir}/)"
    else:
        solution_link = "-"

    return f"| {category} | {number} | {problem_link} | {solution_link} |"


def generate_hints(problems: list[dict]) -> str:
    """힌트 섹션 생성 (빈 템플릿)"""
    lines = []
    for p in problems:
        lines.append(f"- {p['number']}: ")
    return "\n".join(lines)


def build_problem_table(problems: list[dict], solved: dict[int, tuple[str, str]]) -> list[str]:
    """문제 테이블 행 생성 (workbook + 추가 문제)"""
    table_lines = [
        "| 분류 | 번호 | 문제 | 풀이 |",
        "|------|------|------|------|",
    ]

    # workbook 문제 번호 집합
    workbook_numbers = {p["number"] for p in problems}

    # workbook 문제 추가
    for problem in problems:
        num = problem["number"]
        solved_info = solved.get(num)
        solved_dir = solved_info[0] if solved_info else None
        table_lines.append(generate_table_row(num, problem["name"], problem["category"], solved_dir))

    # 추가 문제 (workbook에 없는 로컬 풀이)
    extra_problems = [(num, info) for num, info in solved.items() if num not in workbook_numbers]
    if extra_problems:
        # 번호순 정렬
        extra_problems.sort(key=lambda x: x[0])
        for num, (dir_name, name) in extra_problems:
            table_lines.append(generate_table_row(num, name, "추가 문제", dir_name))

    return table_lines


def generate_readme_content(chapter_id: str, chapter_data: dict, solved: dict[int, tuple[str, str]]) -> str:
    """README 내용 생성"""
    problems = chapter_data["problems"]

    table_lines = build_problem_table(problems, solved)
    problem_table = "\n".join(table_lines)
    hints = generate_hints(problems)

    return README_TEMPLATE.format(
        chapter_id=chapter_id.upper(),
        chapter_name=chapter_data["name"],
        problem_table=problem_table,
        hints=hints,
    )


def update_readme_table(readme_path: Path, chapter_data: dict, solved: dict[int, tuple[str, str]]) -> str:
    """기존 README의 테이블만 업데이트"""
    content = readme_path.read_text(encoding="utf-8")

    # 테이블 찾기 (| 분류 | 번호 | 문제 | 풀이 | 로 시작하는 부분)
    table_pattern = re.compile(
        r"(\| 분류 \| 번호 \| 문제 \| 풀이 \|\n\|[-|]+\|\n)((?:\|[^\n]+\|\n?)+)",
        re.MULTILINE,
    )

    match = table_pattern.search(content)
    if not match:
        return content  # 테이블이 없으면 그대로 반환

    # 새 테이블 생성 (헤더 제외)
    table_lines = build_problem_table(chapter_data["problems"], solved)
    new_table_body = "\n".join(table_lines[2:]) + "\n"  # 헤더 2줄 제외

    new_content = content[: match.start(2)] + new_table_body + content[match.end(2) :]

    return new_content


def process_chapter(chapter_id: str, chapter_data: dict, check_only: bool = False) -> bool:
    """
    단일 챕터 처리
    Returns: 변경이 있었는지 여부
    """
    chapter_dir = ROOT_DIR / chapter_data["dir"]
    readme_path = chapter_dir / "README.md"

    solved = find_solved_problems(chapter_dir)

    if not readme_path.exists():
        # README가 없으면 새로 생성
        if check_only:
            print(f"[NEW] {chapter_id}: README.md 생성 필요")
            return True

        new_content = generate_readme_content(chapter_id, chapter_data, solved)
        chapter_dir.mkdir(parents=True, exist_ok=True)
        readme_path.write_text(new_content, encoding="utf-8")
        print(f"[CREATED] {chapter_id}: README.md 생성됨")
        return True

    # 기존 README 업데이트
    old_content = readme_path.read_text(encoding="utf-8")
    new_content = update_readme_table(readme_path, chapter_data, solved)

    if old_content == new_content:
        print(f"[OK] {chapter_id}: 변경 없음")
        return False

    if check_only:
        print(f"[UPDATE] {chapter_id}: README.md 업데이트 필요")
        return True

    readme_path.write_text(new_content, encoding="utf-8")
    print(f"[UPDATED] {chapter_id}: README.md 업데이트됨")
    return True


def main():
    parser = argparse.ArgumentParser(description="README 자동 생성/업데이트")
    parser.add_argument("chapters", nargs="*", help="처리할 챕터 (예: 0x09)")
    parser.add_argument("--check", action="store_true", help="변경 필요 여부만 확인")
    args = parser.parse_args()

    data = load_problems()
    chapters = data["chapters"]

    # 처리할 챕터 결정
    if args.chapters:
        target_chapters = {k.lower(): v for k, v in chapters.items() if k.lower() in [c.lower() for c in args.chapters]}
    else:
        target_chapters = chapters

    if not target_chapters:
        print("처리할 챕터가 없습니다.")
        sys.exit(1)

    changed = False
    for chapter_id, chapter_data in target_chapters.items():
        if process_chapter(chapter_id, chapter_data, args.check):
            changed = True

    if args.check and changed:
        sys.exit(1)  # pre-commit에서 실패로 처리


if __name__ == "__main__":
    main()
