from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


@dataclass(frozen=True)
class Settings:
    access_key_id: str
    secret_access_key: str
    region: str
    bucket: str
    prefix: str
    notify_url: str


def load_settings() -> Settings:
    access_key_id = os.environ.get("AWS_ACCESS_KEY_ID", "").strip()
    secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY", "").strip()
    region = os.environ.get("AWS_DEFAULT_REGION", "eu-west-1").strip()
    bucket = os.environ.get("PAPERTRAY_BUCKET", "papertray-inbox-prod").strip()
    prefix = os.environ.get("PAPERTRAY_PREFIX", "inbox/").strip()
    notify_url = os.environ.get("PAPERTRAY_NOTIFY_URL", "").strip()
    if not prefix.endswith("/"):
        prefix += "/"

    if not access_key_id or not secret_access_key:
        raise SystemExit("Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in .env")

    return Settings(
        access_key_id=access_key_id,
        secret_access_key=secret_access_key,
        region=region,
        bucket=bucket,
        prefix=prefix,
        notify_url=notify_url,
    )
