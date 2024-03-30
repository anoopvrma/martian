from setuptools import setup, find_packages

setup(
    name='llm_router',
    version='0.1',
    packages=find_packages(),
    description='Python library call LLM models',
    author='Anoop Kumar',
    author_email='anoopvrma@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "providers",
        "anthropic",
        "openai",
        "FastAPI",
        "uvicorn",
        "together"
    ],
)

