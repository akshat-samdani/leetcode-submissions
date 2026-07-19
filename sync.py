#!/usr/bin/env python3
"""Export accepted LeetCode submissions using an encrypted Actions secret."""

import json
import os
import re
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "synced_submissions.json"
SESSION = os.environ.get("LEETCODE_SESSION")

if not SESSION:
    raise RuntimeError("LEETCODE_SESSION is not configured as a repository secret.")

HEADERS = {
    "Cookie": f"LEETCODE_SESSION={SESSION}",
    "User-Agent": "leetcode-submissions-sync/1.0",
    "Accept": "application/json",
}

EXTENSIONS = {
    "python": "py", "python3": "py", "cpp": "cpp", "c": "c", "java": "java",
    "javascript": "js", "typescript": "ts", "csharp": "cs", "golang": "go",
    "kotlin": "kt", "rust": "rs", "swift": "swift", "ruby": "rb", "scala": "scala",
    "php": "php", "mysql": "sql", "mssql": "sql", "oraclesql": "sql", "bash": "sh",
}

DETAIL_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    timestamp
    statusDisplay
    lang { name }
    question { questionId titleSlug title }
  }
}
"""


def request_json(url, payload=None):
    headers = dict(HEADERS)
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    request = Request(url, data=data, headers=headers)
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as error:
        raise RuntimeError(f"LeetCode request failed with HTTP {error.code}.") from error


def safe_name(value):
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", value).strip("-.") or "unknown"


def main():
    previous = set()
    if MANIFEST.exists():
        previous = {int(item) for item in json.loads(MANIFEST.read_text())}

    listing = request_json("https://leetcode.com/api/submissions/?offset=0&limit=5000")
    accepted = [
        item for item in listing.get("submissions_dump", [])
        if item.get("status_display") == "Accepted"
    ]
    pending = sorted(
        (item for item in accepted if int(item["id"]) not in previous),
        key=lambda item: int(item.get("timestamp", 0)),
    )

    for item in pending:
        submission_id = int(item["id"])
        result = request_json(
            "https://leetcode.com/graphql/",
            {"query": DETAIL_QUERY, "variables": {"submissionId": submission_id}},
        )
        detail = result.get("data", {}).get("submissionDetails")
        if not detail or not detail.get("code"):
            raise RuntimeError(f"Could not retrieve code for submission {submission_id}.")

        question = detail["question"]
        language = detail["lang"]["name"]
        extension = EXTENSIONS.get(language, "txt")
        folder = ROOT / "solutions" / safe_name(question["titleSlug"])
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / f"submission-{submission_id}.{extension}"
        target.write_text(detail["code"].rstrip() + "\n", encoding="utf-8")
        print(f"Exported {question['title']} ({language})")
        previous.add(submission_id)

    MANIFEST.write_text(json.dumps(sorted(previous), indent=2) + "\n", encoding="utf-8")
    print(f"Synced {len(pending)} new accepted submission(s).")


if __name__ == "__main__":
    main()
