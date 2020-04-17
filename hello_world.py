import re
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser
# https://github.com/jmcarp/robobrowser
# https://robobrowser.readthedocs.io/en/latest/readme.html

br = RoboBrowser()
print("hello\nworld")