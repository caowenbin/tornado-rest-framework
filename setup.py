# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Extension

setup(
    name='tornado-rest-framework',
    version="0.1.11",
    keywords=("tornado", "asyncio", "rest api", "python3"),
    description='Tornado Rest Framework',
    long_description="Tornado Rest Framework",
    author='caowenbin',
    author_email='cwb201314@qq.com',
    url='https://github.com/caowenbin/tornado-rest-framework',
    download_url='https://github.com/caowenbin/tornado-rest-framework',
    license='BSD',
    packages=["rest_framework"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
       'Programming Language :: Python :: 3.6',
    ],
    scripts=['rest_framework/bin/tornado-admin.py'],
    entry_points={'console_scripts': [
        'tornado-admin = rest_framework.core.script:execute_from_command_line',
    ]},
    ext_modules=[
        Extension(
            "rest_framework.core.router.router",
            ["rest_framework/core/router/router.c"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        ),

        Extension(
            "rest_framework.lib.orm.speedups",
            ["rest_framework/lib/orm/speedups.c"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        ),
    ],
    install_requires=[
        "uvloop==0.10.2"
        "pytz>=2017.3",
        "blinker>=1.4",
        "Babel>=2.5.1",
        "ujson==1.35"
    ]
)
