# How to deploy?

### Docker Dev Environment

1. Run [configure.sh](./docs/configure.sh) to install git and initialize the project
```bash
bash configure.sh
```

2. Refer [nginx.conf](./docs/nginx.conf) for the nginx configurations

3. Use [docker-compose.yml](./docs/docker-compose.yml) for running the application
```bash
sudo docker compose up -d
sudo docker compose logs -f
```