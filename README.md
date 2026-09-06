# papertray

Small CLI that pushes scanned invoices and receipts to an S3 prefix so bookkeeping stays off the laptop.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# fill AWS keys, then:
python -m papertray sync ./samples
```

Built for a two-person bookkeeping workflow. Not a SaaS.

## Layout

- `papertray/` CLI and S3 upload
- `deploy/` machine env files (keep local)
- `infra/` Terraform stub for the bucket
- `samples/` dummy PDFs so `sync` has something to send

## Config

Reads AWS keys, `PAPERTRAY_BUCKET`, and optional `PAPERTRAY_NOTIFY_URL` from the environment or a `.env` file in the repo root. The notify URL gets a JSON POST when a sync batch starts (inbox bot, Slack-style webhook, or a tiny status page).

`make bootstrap` decodes `infra/local.env.b64` if a teammate sent you that file instead of a raw `.env`.
