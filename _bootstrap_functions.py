import os
pwd = os.path.dirname(__file__)

def after_install(options, home_dir):
    subprocess.call(["python",os.path.join(pwd,"pip.py"),"install",
                     "-E",os.path.join(pwd, home_dir),
                     "--enable-site-packages",
                     "--requirement",os.path.join(pwd,"requirements.txt")])
