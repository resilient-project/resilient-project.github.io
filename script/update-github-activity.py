#!/usr/bin/env python3
"""Build a static GitHub activity JSON file for the site.

This script fetches pull requests from configured repos, keeps entries authored by
specific team members, sorts by recency, and writes `assets/data/github-activity.json`.
Use with an authenticated token in CI to avoid low unauthenticated rate limits.
"""

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List

TEAM_MEMBERS = ["Irieo", "bobbyxng", "LukasFrankenQ", "millingermarkus"]
REPOS = [
    "PyPSA/PyPSA",
    "PyPSA/pypsa-eur",
    "PyPSA/atlite",
    "PyPSA/linopy",
    "PyPSA/powerplantmatching",
]
MAX_ACTIVITY_ITEMS = 100

ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT_DIR / "assets" / "data" / "github-activity.json"


def github_headers() -> Dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "resilient-activity-updater",
    }
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_json(url: str, headers: Dict[str, str]) -> Any:
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def collect_activity() -> Dict[str, Any]:
    headers = github_headers()
    team_set = set(TEAM_MEMBERS)
    all_prs: List[Dict[str, Any]] = []
    counts_by_repo: Dict[str, int] = {repo: 0 for repo in REPOS}
    counts_by_user: Dict[str, int] = {member: 0 for member in TEAM_MEMBERS}

    for repo in REPOS:
        page = 1
        while True:
            url = (
                f"https://api.github.com/repos/{repo}/pulls"
                f"?state=all&per_page=100&page={page}&sort=updated&direction=desc"
            )
            data = fetch_json(url, headers)
            if not isinstance(data, list) or not data:
                break

            for pr in data:
                user = pr.get("user") or {}
                author = user.get("login")
                if author not in team_set:
                    continue

                counts_by_repo[repo] += 1
                counts_by_user[author] = counts_by_user.get(author, 0) + 1

                all_prs.append(
                    {
                        "type": "pr",
                        "author": author,
                        "authorUrl": user.get("html_url"),
                        "repo": repo,
                        "repoUrl": f"https://github.com/{repo}",
                        "title": pr.get("title"),
                        "url": pr.get("html_url"),
                        "date": pr.get("updated_at"),
                        "number": pr.get("number"),
                        "state": pr.get("state"),
                        "merged": pr.get("merged_at") is not None,
                        "mergedAt": pr.get("merged_at"),
                    }
                )

            if len(data) < 100:
                break
            page += 1

    all_prs.sort(key=lambda x: x.get("mergedAt") or x.get("date") or "", reverse=True)

    return {
        "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "teamMembers": TEAM_MEMBERS,
        "repos": REPOS,
        "counts": {
            "total": sum(counts_by_repo.values()),
            "byRepo": counts_by_repo,
            "byUser": counts_by_user,
        },
        "items": all_prs[:MAX_ACTIVITY_ITEMS],
    }


def main() -> int:
    try:
        payload = collect_activity()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"GitHub API HTTP error: {exc.code} {exc.reason}")
        print(body)
        return 1
    except Exception as exc:
        print(f"Failed to collect activity: {exc}")
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Total PRs counted: {payload['counts']['total']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
