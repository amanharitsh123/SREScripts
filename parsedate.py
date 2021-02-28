import subprocess
import regex
# run command and obtain output
out = subprocess.Popen(["date"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, stderr = out.communicate()

# encoding string from binary to ascii
date_output = stdout.decode("ascii")

# use regex to parse string

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
months = ["Jan", "Feb", "Mar"]

pattern = r'\L<day> \L<month>'

p = regex.compile(pattern, regex.X, day=days, month=months)
s = "Sun Jan"
print(p.search(pattern, s).group())
