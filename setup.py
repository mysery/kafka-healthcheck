import setuptools

meta = {}

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("kafka_healthcheck/version.py") as f:
    exec(f.read(), meta)

requires = [
]

setuptools.setup(
    name="kafka-healthcheck",
    version=meta["__version__"],
    author="Rodrigo Garcia fork of Shawn Seymour",
    author_email="rodrigo.garcia@despgar.com",
    description="A simple healthcheck wrapper to monitor kafka with kafkacat.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rodrigongarcia/kafka-healthcheck",
    license="Apache License 2.0",
    packages=["kafka_healthcheck"],
    install_requires=requires,
    entry_points={
        "console_scripts": ["kafka-healthcheck=kafka_healthcheck.main:main"],
    },
    keywords=("kafka", "health", "healthcheck", "wrapper", "monitor", "kafkacat", "kcat"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
