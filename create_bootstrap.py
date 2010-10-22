#Create a bootstrap script
import os
import virtualenv

pwd = os.path.dirname(os.path.abspath(__file__))
script_name = os.path.join(pwd, 'bootstrap.py')
extra_text = open(os.path.join(pwd,'_bootstrap_functions.py')).read()

def main():
    text = virtualenv.create_bootstrap_script(extra_text)
    if os.path.exists(script_name):
        print "bootstrap script already exists..."
        f = open(script_name)
        cur_text = f.read()
        f.close()
    else:
        cur_text = ''
        print 'Updating %s' % script_name
    if cur_text == text:
        print 'bootstrap function still the same, no update...'
    else:
        print 'Script changed; updating...'
        f = open(script_name, 'w')
        f.write(text)
        f.close()

if __name__ == '__main__':
    main()
