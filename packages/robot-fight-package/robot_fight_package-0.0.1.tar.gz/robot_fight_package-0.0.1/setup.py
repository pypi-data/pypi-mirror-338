from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="robot-fight-package",
    version="0.0.1",
    author="Cleiton",
    author_email="cleitonguilhermite@gmail.com",
    description="Simulação de combate entre robôs lutadores",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Draky-Rollgard/Robot_Fight",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.12.9',
)