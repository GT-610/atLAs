# Necessary variables
home = os.getenv('HOME')
atlas_home = os.path.join(home,".config/atlas/")
temp_path  = os.path.join(atlas_home, "tmp/")
image_path = os.path.join(atlas_home, "images/")
container_path = atlas_home + "containers/"
registries_path = atlas_home + 'registries/'
ver = '2.99.0'

# Check system architecture
def check_arch():
    arch = os.uname().machine
    if arch == 'aarch64' or 'armv8' in arch:
        arch = 'aarch64'
    elif '86' in arch:
        arch = 'i386'
    elif 'arm' in arch:
        arch = 'arm'
    return arch

arch = check_arch()