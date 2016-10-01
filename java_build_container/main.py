import os
import shutil

TASK_NAME = 'java-build'


def run_cmd(app_dir, out_dir):
    os.system('docker run --rm -v {app_dir}:/app -w /app maven:3-jdk-8 mvn clean install'.format(app_dir = app_dir))


def main():
    app_dir = os.environ['APP_DIR']
    parent_out_dir = os.environ.get('PARENT_OUT_DIR', '')
    out_dir = parent_out_dir + os.path.sep + 'java-build'

    shutil.rmtree('/app/' + out_dir, ignore_errors=True)
    os.mkdir('/app/' + out_dir)

    run_cmd(app_dir, out_dir)

    open('/app/' + out_dir + '/java-build.out', 'w+')
    print 'Java-build finished'

if __name__ == '__main__':
    main()
