# hackathon

## Execute

From project root directory run:
```bash
docker run --rm -v $PWD:/app -e "APP_DIR=${PWD}" -v /var/run/docker.sock:/var/run/docker.sock seed
```