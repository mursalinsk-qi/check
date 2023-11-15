import os
import re
import sys


def check_test_files():
    if(os.path.exists('cover.out')):
        for path, directory, files in os.walk("internal"):
            go_files = [i for i in files if re.search(".go$", i)]
            go_test_files = [i for i in files if re.search("_test.go$", i)]
            if len(go_files) > 0 and len(go_test_files) <= 0:
                sys.exit("Inadequate test coverage. Please improve test coverage.")
    else:
        sys.exit("cover.out not present")
        
        
check_test_files()
