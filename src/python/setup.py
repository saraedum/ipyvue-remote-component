from setuptools import setup

setup(**{
    'name': 'ipyvue_remote_component',
    'version': '0.1.0',
    'description': 'Load Vue Components for ipyvue at Runtime',
    'long_description': 'Load Vue Components for ipyvue at Runtime',
    'include_package_data': True,
    'data_files': [
        ('share/jupyter/nbextensions/ipyvue-remote-component', [
            'generated/notebook/javascript/extension.js',
            'generated/notebook/javascript/widget.js',
            'generated/notebook/javascript/widget.js.map',
        ],),
        ('etc/jupyter/nbconfig/notebook.d' ,['assets/notebook/ipyvue-remote-component.json'])
    ],
    'install_requires': [
        'ipyvue',
    ],
    'packages': ['ipyvue_remote_component'],
    'zip_safe': False,
    'author': 'Julian Rüth',
    'author_email': 'julian.rueth@fsfe.org',
    'url': 'https://github.com/saraedum/ipyvue-remote-component',
    'keywords': [
        'ipython',
        'jupyter',
        'widgets',
        'vue',
    ],
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
})
