from setuptools import setup, find_packages


with open("README.md", "r", encoding="UTF-8") as file:
    readme = file.read()


requirements = ["asyncio>=3", "aiohttp>=3"]


setup(
    name="async_VKsher",
    version="2.3.0",
    author="Kulenov Islam",
    author_email="kit.werr34@gmail.com",
    description="asyncVK is asynchronous library for creating a bot in VK",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Ekventor/asyncVK",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    keywords="vk vkontakte вк вконтакте бот bot api vk_api"
)
