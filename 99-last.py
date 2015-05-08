import glob
import os

print("""\n\n=============================\nInitialization commands:\n=============================\n""")

home = os.environ['HOME']

flist = glob.glob(home+'/.ipython/profile_default/startup/*.py')
flist.pop()

for f in flist:
    fid = open(f)
    print('*** File {} initialized:\n'.format(f))
    print(fid.read())
    fid.close()

print("""=============================""")
