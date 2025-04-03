from os import path
from setuptools import setup, find_packages
from setuptools.command.sdist import sdist

from co6co import setupUtils
packages = find_packages()
packageName = packages[0]


def get_version():
    package_dir = path.abspath(path.dirname(__file__))
    version_file = path.join(package_dir, packageName, '__init__.py')
    with open(version_file, "rb") as f:
        source_code = f.read()
    exec_code = compile(source_code, version_file, "exec")
    scope = {}
    exec(exec_code, scope)
    version = scope.get("__version__", None)
    if version:
        return version
    raise RuntimeError("Unable to find version string.")


# read readmeFile contents
currentDir = path.abspath(path.dirname(__file__))
with open(path.join(currentDir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class CustomSdist(sdist):
    def get_archive_files(self):
        # 获取原始的文件名列表
        files = super().get_archive_files()
        new_files = []
        for file in files:
            # 替换文件名中的 _ 为 .
            new_file = file.replace(self.distribution.get_name().replace('.', '_'), self.distribution.get_name())
            new_files.append(new_file)
        return new_files


version = setupUtils.get_version(__file__)
packageName, packages = setupUtils.package_name(__file__)
long_description = setupUtils.readme_content(__file__)

setup(
    name=packageName,
    version=version,
    description="web permissionsAPI",
    packages=packages,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    include_package_data=True, zip_safe=True,
    # 依赖哪些模块
    install_requires=['requests', "co6co>=0.0.25", "co6co.sanic_ext>=0.0.9", "co6co.web-db>=0.0.14", "opencv-python==4.11.0.86", "numpy==1.26.4", "Pillow>=10.1.0"],
    # package_dir= {'utils':'src/log','main_package':'main'},#告诉Distutils哪些目录下的文件被映射到哪个源码
    author='co6co',
    author_email='co6co@qq.com',
    url="http://github.com/co6co",
    data_file={
        ('', "*.txt"),
        ('', "*.md"),
    },
    package_data={
        '': ['*.txt', '*.md'],
        'bandwidth_reporter': ['*.txt']
    }, cmdclass={
        'sdist': setupUtils.CustomSdist
    }
)
