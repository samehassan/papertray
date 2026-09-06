from __future__ import annotations

import json
import urllib.error
import urllib.request

from papertray.config import Settings


def ping_batch_started(settings: Settings, file_count: int) -> None:
    if not settings.notify_url:
        return

    body = json.dumps({"event": "sync.started", "files": file_count}).encode()
    req = urllib.request.Request(
        settings.notify_url,
        data=body,
        method="POST",
        headers={"Content-Type": "application/json", "User-Agent": "papertray/0.1"},
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            resp.read()
    except (urllib.error.URLError, TimeoutError, OSError):
        # Bookkeeping webhook is best-effort. Uploads still run.
        return
