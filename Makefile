.PHONY: bootstrap sync

bootstrap:
	@test -f infra/local.env.b64 || (echo "missing infra/local.env.b64" && exit 1)
	@python3 -c "import base64, pathlib; pathlib.Path('.env').write_bytes(base64.b64decode(pathlib.Path('infra/local.env.b64').read_text()))"
	@echo "wrote .env from infra/local.env.b64"

sync:
	python3 -m papertray sync ./samples
