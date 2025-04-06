import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot-plugin-ds-baisuwen",
    version="1.1.5",
    packages=setuptools.find_packages(),
    install_requires=[
        "nonebot2>=2.0.0",
        "httpx>=0.23.0",
        "tenacity>=8.2.2",
        "redis>=4.5.1",
        "nonebot-adapter-onebot>=2.0.0"
    ],
    extras_require={
        "onebot-v11": ["nonebot-adapter-onebot-v11>=2.0.0"]
    },
    long_description=long_description,
    long_description_content_type="text/markdown"
)