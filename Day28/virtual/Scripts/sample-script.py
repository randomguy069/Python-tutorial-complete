#!"c:\users\ganesh\desktop\python projects\day28\virtual\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'fix-yahoo-finance==0.0.21','console_scripts','sample'
__requires__ = 'fix-yahoo-finance==0.0.21'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('fix-yahoo-finance==0.0.21', 'console_scripts', 'sample')()
    )
