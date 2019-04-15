Run a local (dev) instance just by running start_dev.sh, you will need a working docker compose on your machine.

start_dev.sh \<option\>
    
- makemigrations: make django migrations

- migrate: migrate local dev database (happens automatically when starting the dev environment)

- bash: run bash in container

- csu: create super user

- test: run django tests