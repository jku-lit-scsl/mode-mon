from distutils.core import setup

from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['admon_mode_cps_pkg', 'python_statemachine', 'paho_mqtt'],
    package_dir={'': 'src'}
)
setup(**d)
