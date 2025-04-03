from setuptools import setup, find_packages

setup(
    name="ControllerMixing",  # <-- change this
    version="0.1.1",
    description="Fit proportional-integral controllers and estimate mixing coefficients.",
    author="Justin Michael Fine",
    author_email="justfineneuro@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "matplotlib",
        "numpy",
        "jax[cpu]",
        "numpyro",
        "mat73",
        "scipy",
        "ruptures",
        "dill",
        "tqdm",
        "optax",
    ],
    python_requires=">=3.8",
)