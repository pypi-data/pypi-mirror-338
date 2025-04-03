from setuptools import setup, find_packages

setup(
    name="meetscribe",
    version="0.1.1",
    author="Anish Bipin Jagadale",
    author_email="jagdaleanish@gmail.com",
    description="An intelligent audio-to-transcript chatbot powered by Whisper, PyAnnote, FAISS, and LLMs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jagadale1234/meetscribe",  # Optional: link to your GitHub repo
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
        "openai-whisper",
        "torch",
        "torchaudio",
        "pyannote.audio",
        "faiss-cpu",  
        "langchain",
        "langchain-community",
        "langchain-openai",
        "transformers",
        "sentence-transformers",
        "llama-index"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.10",
    entry_points={
    'console_scripts': [
        'meetscribe=meetscribe.main:main',
    ],
},
)
