from setuptools import setup, find_packages

setup(
    name="simpletts",
    description="Easily run and use TTS models with just a few lines of code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fakerybakery/simpletts",
    author="mrfakename",
    author_email="me@mrfake.name",
    license="BSD-3-Clause",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "accelerate",
        "torchaudio",
        "transformers[torch]",
        "datasets",
        "pydub",
        "numpy",
        "scipy",
        "librosa",
        "soundfile",
        "tqdm",
        "click",
    ],
    extras_require={
        "xtts": [
            "tts",
        ],
    },
)
