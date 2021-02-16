from __future__ import print_function
from setuptools import setup, find_packages
import os
from os.path import join as pjoin
from distutils import log

from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
)


here = os.path.dirname(os.path.abspath(__file__))

log.set_verbosity(log.DEBUG)
log.info('setup.py entered')
log.info('$PATH=%s' % os.environ['PATH'])

name = 'ipyvue_remote_component'
LONG_DESCRIPTION = 'Load Vue.js Packages at Runtime in Jupyter Notebooks and JupyterLab'

js_dir = pjoin(here, 'js')

# Representative files that should exist after a successful build
jstargets = [
    pjoin(js_dir, 'dist', 'index.js'),
]

data_files_spec = [
    ('share/jupyter/nbextensions/ipyvue-remote-component', 'ipyvue_remote_component/nbextension', '*.*'),
    ('share/jupyter/labextensions/ipyvue-remote-component', 'ipyvue_remote_component/labextension', "**"),
    ("share/jupyter/labextensions/ipyvue-remote-component", '.', "install.json"),
    ('etc/jupyter/nbconfig/notebook.d', '.', 'ipyvue-remote-component.json'),
]

cmdclass = create_cmdclass('jsdeps', data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(js_dir, npm=['yarn'], build_cmd='build:prod'), ensure_targets(jstargets),
)

setup_args = dict(
    name=name,
    version="1.0.0",
    description='Load Vue.js Packages at Runtime in Jupyter Notebooks and JupyterLab',
    long_description=LONG_DESCRIPTION,
    include_package_data=True,
    install_requires=[
        'ipywidgets>=7.6.0',
        'ipyvue>=1.5.0',
    ],
    packages=find_packages(),
    zip_safe=False,
    cmdclass=cmdclass,
    author='Julian Rüth',
    author_email='julian.rueth@fsfe.org',
    url='https://github.com/saraedum/ipyvue-remote-component',
    keywords=[
        'ipython',
        'jupyter',
        'widgets',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

setup(**setup_args)
