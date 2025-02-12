import json
from pathlib import Path

from parse_scripts import bandit

TEST_DIR = Path(__file__).parent
JSON_DIR = TEST_DIR / "json"


def test_errors():
    results = json.loads(Path(JSON_DIR / "bandit_error.json").read_text())
    errors = [bandit.bandit_error(error) for error in results["errors"]]
    assert errors[0]["path"] == "LICENSE"
    assert errors[1] == {
        "path": "tests/data/py2.py",
        "start_line": 2,
        "end_line": 2,
        "annotation_level": "failure",
        "title": "invalid syntax",
        "message": "Missing parentheses in call to 'print'. Did you mean print(...)?",
    }


def test_annotations():
    results = json.loads(Path(JSON_DIR / "bandit.json").read_text())
    annotations = bandit.bandit_annotations(results)
    assert annotations[0]["path"] == "canary.py"
    assert annotations[0]["start_line"] == 3


def test_run_check():
    results = json.loads(Path(JSON_DIR / "bandit.json").read_text())
    run_check_body = bandit.bandit_run_check(results)
    assert run_check_body["conclusion"] == "failure"
