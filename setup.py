import setuptools

with open('README.md') as f:
    text = f.read()

setuptools.setup(
    name="async_yandex_checkout",
    version="0.0.1",
    author="yank0vy3rdna",
    author_email="yankovyerdna@yandex.ru",
    description="Yandex checkout async api wrapper",
    long_description=text,
    long_description_content_type="text/markdown",
    license="GPLv3",
    url="https://github.com/yank0vy3rdna",
    packages=["aio_yandex_translate"],
    package_dir={"aio_yandex_translate": ""},
    install_requires=["aiohttp>=3.6", "aiohttp-proxy>=0.1.2"],
    extras_require={"ujson": ""},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">=3.6"
)