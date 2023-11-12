import subprocess

if __name__ == '__main__':
    s = subprocess.run('behave -f html -o reports/temp.html --tags=temp', shell=True, check=True)
