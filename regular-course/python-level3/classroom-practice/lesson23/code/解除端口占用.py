import os
import subprocess


def kill_process_on_port(port):
    # 在 windows 电脑上
    if os.name == 'nt':
        command = f'netstat -ano | findstr :{port}'
        process_info = subprocess.check_output(command, shell=True, encoding='utf-8').strip()
        print(process_info)
        if process_info != '':
            pid = process_info.split()[-1]
            subprocess.run(f'taskkill /pid {pid} /f', shell=True, stdout=subprocess.DEVNULL)
            print(f'Killed process with PID {pid}')
        else:
            print(f'No process is running on port {port}')
    # 在Mac电脑上
    else:
        command = f'netstat -nav | grep {port} | awk \'{{print $9}}\' | cut -d \'.\' -f 1'
        process_info = os.popen(command).read().strip().split('\n')[1:]
        if process_info != ['']:
            for process in process_info:
                pid = process.split()[1]
                os.system(f'kill -9 {pid}')
        else:
            print(f'No process is running on port {port}')


# 用法示例
kill_process_on_port(10051)
