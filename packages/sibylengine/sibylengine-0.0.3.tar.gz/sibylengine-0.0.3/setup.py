from setuptools import setup

setup(
    name="sibylengine",
    version='0.0.3',
    description='Custom Vulkan renderer',
    include_package_data=True,
    python_requires = "==3.8.18",
    install_requires=[
        'torch==2.1.1+cu118',
    ],
)
