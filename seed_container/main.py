import strictyaml
import os

SEED_FILE="/app/seed.yml"

def run_pipeline(name):
    os.system("docker run --rm -v /app:/app -v /var/run/docker.sock:/var/run/docker.sock {}".format(name))

def main():
    with open(SEED_FILE, 'r') as file:
        seed = strictyaml.load(file.read())
    run_pipeline(seed['pipeline'])
    print 'Finish'

if __name__ == '__main__':
    main()
