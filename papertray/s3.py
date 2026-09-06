from __future__ import annotations

from pathlib import Path

import boto3

from papertray.config import Settings


def client(settings: Settings):
    return boto3.client(
        "s3",
        region_name=settings.region,
        aws_access_key_id=settings.access_key_id,
        aws_secret_access_key=settings.secret_access_key,
    )


def upload_file(settings: Settings, path: Path) -> str:
    key = f"{settings.prefix}{path.name}"
    client(settings).upload_file(str(path), settings.bucket, key)
    return key
