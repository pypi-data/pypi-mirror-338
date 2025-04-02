from setuptools import setup, find_packages

setup(
    name="pasargadbot",
    version="2.0.0",
    author="ramox",
    author_email="actramox@gmail.com",
    description="یک کتابخانه ضد ربات قوی برای وبسایت‌ها",
    packages=find_packages(),
    install_requires=['Flask>=2.0.0'],
    python_requires='>=3.6',
)