compose: ## Starts up both client and server
	docker compose up

client: ## Starts up the client
	docker compose start client

server: ## Starts up the server
	docker compose start server

help: ## Shows this help
	@grep -E '^[.a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'