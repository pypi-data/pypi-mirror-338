import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setuptools.setup(
        name="genialn",  # Измените имя пакета на genialn
        version="0.0.1",
        author="NEFOR",
        author_email="genialNEFOR@gmail.com",
        description="A simple library for speed control in Python.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/your_username/genial",  # URL вашего репозитория на GitHub (если есть)
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )
