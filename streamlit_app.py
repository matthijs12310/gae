import os
import requests
url = 'https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v1.62.2/openvscode-server-v1.62.2-linux-x64.tar.gz'
r = requests.get(url, allow_redirects=True)
open('openvscode-server-v1.62.2-linux-x64.tar.gz', 'wb').write(r.content)
os.system("tar -xzf openvscode-server-v1.62.2-linux-x64.tar.gz && cd openvscode-server-v1.62.2 && ./server.sh")
