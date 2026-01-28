"""
Pre-commit hook: 새 풀이 추가 시 README 자동 업데이트 및 problems.json 갱신

설치 방법:
    # Unix (macOS/Linux)
    ln -sf ../../scripts/pre-commit-hook.sh .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit

    # Windows (Git Bash / PowerShell)
    cp scripts/pre_commit_hook.py .git/hooks/pre-commit
"""

import json
import re
import subprocess
import sys
from pathlib import Path

# 스크립트 경로 설정
SCRIPT_DIR = Path(__file__).parent.resolve()
ROOT_DIR = SCRIPT_DIR.parent
PROBLEMS_JSON = SCRIPT_DIR / "problems.json"


def run_command(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """명령어 실행"""
    return subprocess.run(cmd, capture_output=True, text=True, check=check)


def get_staged_files() -> list[str]:
    """스테이징된 새 파일 목록"""
    result = run_command(["git", "diff", "--cached", "--name-only", "--diff-filter=A"])
    files = result.stdout.strip().split("\n")
    # 따옴표 제거
    return [f.strip('"') for f in files if f]


def extract_chapter_id(file_path: str) -> str | None:
    """파일 경로에서 챕터 ID 추출"""
    match = re.match(r"^(0x[0-9a-fA-F]+)\. ", file_path)
    if match:
        return match.group(1).lower()
    return None


def chapter_exists_in_json(chapter_id: str) -> bool:
    """problems.json에 챕터가 있는지 확인"""
    if not PROBLEMS_JSON.exists():
        return False
    content = PROBLEMS_JSON.read_text(encoding="utf-8")
    return f'"{chapter_id}":' in content


def run_uv_script(script_name: str, args: list[str]) -> bool:
    """uv로 Python 스크립트 실행"""
    script_path = SCRIPT_DIR / script_name
    cmd = ["uv", "run", str(script_path)] + args

    try:
        result = subprocess.run(cmd, cwd=ROOT_DIR, check=False)
        return result.returncode == 0
    except FileNotFoundError:
        # uv가 없으면 python으로 시도
        cmd = [sys.executable, str(script_path)] + args
        result = subprocess.run(cmd, cwd=ROOT_DIR, check=False)
        return result.returncode == 0


def git_add(file_path: Path) -> None:
    """파일 스테이징"""
    run_command(["git", "add", str(file_path)], check=False)


def main() -> int:
    # 스테이징된 파일에서 챕터 찾기
    staged_files = get_staged_files()

    changed_chapters = set()
    for file_path in staged_files:
        chapter_id = extract_chapter_id(file_path)
        if chapter_id:
            changed_chapters.add(chapter_id)

    if not changed_chapters:
        return 0  # 변경된 챕터 없음

    # 새 챕터 찾기 (problems.json에 없는 것)
    new_chapters = [ch for ch in changed_chapters if not chapter_exists_in_json(ch)]

    # 새 챕터 fetch
    if new_chapters:
        print(f"🔍 새 단원 감지: {' '.join(new_chapters)}")
        print("📥 Workbook에서 문제 목록 가져오는 중...")

        for chapter_id in new_chapters:
            if not run_uv_script("fetch_problems.py", [chapter_id]):
                print(f"⚠️  {chapter_id}: workbook fetch 실패 (수동으로 problems.json 업데이트 필요)")

        # problems.json 스테이징
        if PROBLEMS_JSON.exists():
            git_add(PROBLEMS_JSON)
            print("✅ problems.json 스테이징됨")

    # README 업데이트
    print(f"📝 README 업데이트 중: {' '.join(changed_chapters)}")

    if not run_uv_script("generate_readme.py", list(changed_chapters)):
        print("❌ README 업데이트 실패")
        return 1

    # 업데이트된 README 스테이징
    if PROBLEMS_JSON.exists():
        with open(PROBLEMS_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)

        for chapter_id in changed_chapters:
            chapter_data = data.get("chapters", {}).get(chapter_id, {})
            chapter_dir = chapter_data.get("dir", "")

            if chapter_dir:
                readme_path = ROOT_DIR / chapter_dir / "README.md"
                if readme_path.exists():
                    git_add(readme_path)
                    print(f"✅ {chapter_dir}/README.md 스테이징됨")

    print("✨ 완료")
    return 0


if __name__ == "__main__":
    sys.exit(main())
