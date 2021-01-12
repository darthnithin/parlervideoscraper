import re
import os
with open ("li.txt", "r") as myfile:
    data=myfile.readlines()

for i in data:
    print(i)
    regex = r"meta-(.*).json"
    m = re.findall(regex, i)
    jk = ''.join(m)
    kl = jk[0:2]
    zx = jk[2:4]
    c = f'curl -O --resolve video.parler.com:443:8.253.139.116 https://video.parler.com/{kl}/{zx}/{jk}.mp4'
    os.system(c)
