import os
import wget
url = 'https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v1.62.2/openvscode-server-v1.62.2-linux-x64.tar.gz'
filename = wget.download(url)
filename
os.system("ls")
