'''

pip install deepface tf-keras -i https://pypi.tuna.tsinghua.edu.cn/simple

'''
import subprocess
import sys
import shutil
import os

result = subprocess.run("pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple", shell=True,
                        stdout=subprocess.PIPE)
print("*" * 30)
python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
print(f"您正在为该路径：{sys.executable}下的python安装第三方库")
if float(python_version) < 3.8:
    print('但是它的版本小于3.8，请重新选择版本大于等于3.8的python')
    exit()
subprocess.call(f'{sys.executable} -m pip install --upgrade pip', shell=True)
lib_names = ['deepface', 'tf-keras']
for lib in lib_names:
    result = subprocess.call(f'{sys.executable} -m pip install {lib}', shell=True)
    if result == 0:
        print(f"{lib} 安装成功.")
    else:
        print(f"{lib} 安装失败.")

src_folder = os.path.join(os.getcwd(), '.deepface')
home_dir = os.path.expanduser('~')

dst_folder = os.path.join(home_dir, '.deepface')

if os.path.exists(dst_folder):
    shutil.rmtree(dst_folder)
shutil.copytree(src_folder, dst_folder)
