from setuptools import setup, find_packages

setup(
    name="polydevenc",  # تم تغيير الاسم هنا
    version="0.1",
    description="A simple encryption tool",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author="Karim Elyamani",
    author_email="karimalyamani20@gmail.com",
    packages=find_packages(where='src'),
    package_dir={"": "src"},  # التأكد من أن الحزمة في مجلد src
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
