'''
Bootstrap include script created with simple-bootstrap & virtualenv
- This scripts sets up a virtualenv
- Install packages using pip, checks "requirements/" dir for .txt files and installs all packages listed in the .txt
- http://github.com/zyelabs/simple-bootstrap
'''
import glob


def get_ordered_files(path):
    f = []
    for ifile in glob.glob( os.path.join(path,"requirements", '*.txt') ):

        if ifile.find("local")>-1:
            f.append((0,ifile))
        elif ifile.find("required")>-1:
            f.append((1,ifile))
        elif ifile.find("optional")>-1:
            f.append((3,ifile))
        else:
            f.append((2,ifile))
    f.sort()
    return f

def after_install(options, home_dir):
    pwd = os.path.dirname(os.path.abspath(__file__))
    if sys.platform == 'win32':
        bin = "Scripts"
        cmd_list = [os.path.join(home_dir,bin,"pip"), "install",
                 "-E",os.path.join(pwd, home_dir),
                 "--enable-site-packages",
                 "--requirement"]
    else:
        bin = "bin"
        cmd_list = ["python",os.path.join(pwd,"pip.py"), "install",
                 "-E",os.path.join(pwd, home_dir),
                 "--enable-site-packages",
                 "--requirement"]
        try:
            import pip
            try:
                print "Found pip, moving along".ljust(50,'.')
                f = open('pip.py', 'r')
            except:
                print os.path.join(pwd, home_dir)
                print "Found pip, moving along".ljust(50,'.')
                cmd_list = ["pip", "install",
                 "-E",os.path.join(pwd, home_dir),
                 "--enable-site-packages",
                 "--requirement"]
        except:
            print "Downloading pip".ljust(50,'.')
            import urllib2
            fileurl = "http://github.com/downloads/zyelabs/simple-bootstrap/pip.py"
            tofile = os.path.join(pwd,"pip.py")
            u = urllib2.urlopen(fileurl)
            localFile = open(tofile, 'w')
            localFile.write(u.read())
            localFile.close()
    print "Installing Requirements".ljust(50,'.')
    files = get_ordered_files(pwd)
    subprocess.call(["python", os.path.join(home_dir,bin,"activate_this.py")])
    for f in files:
        print "Requirements file ", f[1]
        print ''.ljust(50,'.')
        file_cmd = cmd_list + [f[1]]
        subprocess.call(file_cmd)
    print "Done"