from setuptools import setup, find_packages

setup(
    name="pretix_custom_head",
    version="0.1.8",
    description="A Pretix plugin to inject custom code into the <head> section and track events using Plausible Analytics.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Bergruebe",
    author_email="68869895+Bergruebe@users.noreply.github.com",
    url="https://github.com/bergruebe/pretix_custom_head",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=3.2",
        "pretix>=3.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "pretix.plugin": [
            "pretix_custom_head = pretix_custom_head:PretixPluginMeta",
        ],
    },
)