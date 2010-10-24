import os, sys, subprocess, textwrap, glob

ROOT        = os.path.dirname(os.path.abspath(__file__))
VENV_URL    = "http://github.com/downloads/zyelabs/simple-bootstrap/virtualenv.py"


def setup(project = "TESTING"):
    try:
        import virtualenv
    except:
        print 'Downloading VirtualEnv Package'.ljust(50,'.'),
        loc_venv = os.path.join(ROOT, 'virtualenv.py')
        download(VENV_URL,loc_venv)
        print 'Done\n'
        import virtualenv
        
    
    print 'Creating Bootstrap'.ljust(50,'.'),
    #extra_text = open(os.path.join(ROOT,'bootstrap_addon.py')).read()
    extra_text = textwrap.dedent('''
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
        print "Installing Requirements".ljust(50,'.')
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
        files = get_ordered_files(pwd)
        subprocess.call(["python", os.path.join(home_dir,bin,"activate_this.py")])
        for f in files:
            print "Installing from", f[1], ''.ljust(50,'.')
            cmd_list.append(f[1])
            subprocess.call(cmd_list)
        print "Done"  ''')
    bootstrap_text = virtualenv.create_bootstrap_script(extra_text)
    f = open('bootstrap.py', 'w').write(bootstrap_text)
    print 'Done\n'
    print 'Executing Bootstrap'.ljust(50,'.')
    
    subprocess.call(["python", "bootstrap.py",project ])
    print 'Done\n'
    
    print 'Environment Has been setup'.ljust(50,".")

    
def download(fileurl, tofile):
    import urllib2
    u = urllib2.urlopen(fileurl)
    localFile = open(tofile, 'w')
    localFile.write(u.read())
    localFile.close()      

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Please specify destination folder name as first argument'
    else:
        setup(str(sys.argv[1]))


