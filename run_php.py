import subprocess


def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if stdout:
        stdout = stdout.rstrip()
    if stderr:
        stderr = stderr.rstrip()
    return stdout, stderr, p.returncode


def encrypt(string, operation):
    a, b, c = run_cmd(f'php encrypt.php {string} {operation}')
    return a.decode('utf-8')


if __name__ == '__main__':
    print(encrypt('anything', 'encrypt'))

""" 
<?php
$string = $argv[1];
$operation = $argv[2];
function encrypt($string,$operation,$key='casio'){
    if($operation == 'encrypt'){
        echo 'do something';
    } else {
        echo 'else';
    }
}
 """
