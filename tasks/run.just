set working-directory := '..'

[private]
default:
    @just --list run

[doc("Start the docker compose infrastructure for development")]
compose profile="dev":
    docker compose --profile {{profile}} up -d --build --wait


[doc('Start the development server.')]
dev port="8008":
    @just run compose dev
    uv run backend run --port {{port}} --reload

[doc('Start the production server.')]
prod:
    @just run compose prod

[doc("Stop all docker containers.")]
stop:
    docker compose --profile "*" down
