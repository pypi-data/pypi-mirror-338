from setuptools import setup, find_packages

setup(
    name="pasargadbot",
    version="0.1.0",
    author="ramox",
    author_email="actramox@gmail.com",
    description="یک کتابخانه ضد ربات برای وبسایت‌ها",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pasargadcdn",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=2.0.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)