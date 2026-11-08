import urllib.request
import re

req = urllib.request.Request("https://www.espncricinfo.com/cricketer/virat-kohli-253802", headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
match = re.search(r'https://img1\.hscicdn\.com/image/upload/[^"]*', html)
if match: print("Virat:", match.group())

req = urllib.request.Request("https://www.espncricinfo.com/cricketer/ms-dhoni-28081", headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
match = re.search(r'https://img1\.hscicdn\.com/image/upload/[^"]*', html)
if match: print("Dhoni:", match.group())

req = urllib.request.Request("https://www.espncricinfo.com/cricketer/rohit-sharma-34102", headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
match = re.search(r'https://img1\.hscicdn\.com/image/upload/[^"]*', html)
if match: print("Rohit:", match.group())
