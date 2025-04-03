from setuptools import setup, find_packages

setup(
    name="ControllerMixing",  # <-- change this
    version="0.1.0",
    description="Fit proportional-integral controllers and estimate mixing coefficients.",
    author="Justin Michael Fine",
    author_email="justfineneuro@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas~=1.5.3",
        "matplotlib~=3.7.0",
        "numpy~=1.23.5",
        "jax~=0.4.30",
        "numpyro~=0.18.0",
        "mat73~=0.65",
        "scipy~=1.12.0",
        "ruptures~=1.1.9",
        "dill~=0.3.6",
        "tqdm~=4.64.1",
        "optax~=0.2.3",
    ],
    python_requires=">=3.8",
)