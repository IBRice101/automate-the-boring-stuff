import os

os.chdir('/run/media/isaac/IBRICE/Misc/Non-Uni/ATBSWP')

for filename in os.listdir():
    if filename.endswith('.md'):
        #os.unlink(filename)
        print(filename)
