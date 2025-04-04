import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="genialn",  # Обязательно: Имя пакета
    version="0.0.2",  # **ОБЯЗАТЕЛЬНО:** Увеличьте номер версии!
    author="NEFOR",  # Замените на свое имя
    author_email="GENIAL@gmail.com",  # Замените на свой email
    description="A simple library for speed control in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/genial",  # URL вашего репозитория на GitHub (если есть)
    packages=setuptools.find_packages(),  # Автоматически находит все пакеты в проекте
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Минимальная версия Python
)
