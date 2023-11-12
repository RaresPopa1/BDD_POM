import subprocess

if __name__ == '__main__':
    s = subprocess.run('behave -f html -o reports/regression.html --tags=regression', shell=True, check=True)
