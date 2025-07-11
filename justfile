mod run 'tasks/run.just'

[private]
default:
    @just --list


[doc("Install dependencies")]
install:
    @echo "Installing dependencies"
    uv sync --dev --frozen --link-mode=copy --all-extras
    uv run pre-commit install --overwrite --install-hooks

[doc("Upgrade dependencies")]
upgrade:
    @echo "Upgrading dependencies"
    uv lock --upgrade --link-mode=copy
    @just install

[doc("Lint the project files")]
lint:
    uv run pre-commit run ruff --all-files
    uv run pre-commit run ruff-format --all-files
    uv run pre-commit run mypy --all-files
    uv run pre-commit run end-of-file-fixer --all-files
    uv run pre-commit run codespell --all-files

[doc("Run pytest with arguments")]
test *args:
    uv run pytest {{ args }}



[doc("Build and scan image.")]
build tag="python-template":
	docker build -f Dockerfile -t {{tag}} .
