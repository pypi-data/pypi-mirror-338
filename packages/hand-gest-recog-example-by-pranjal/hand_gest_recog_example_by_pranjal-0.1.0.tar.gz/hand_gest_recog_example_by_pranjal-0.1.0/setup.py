from setuptools import setup, find_packages

setup(
    name="hand_gest_recog_example_by_pranjal",  # Your package name
    version="0.1.0",
    packages=find_packages(),  # Automatically finds `hand_gesture`
    install_requires=[
        "mediapipe",  # Add more dependencies from requirements.txt
        "opencv-python",
    ],
    author="Pranjal Prabhat",
    description="A hand gesture recognition example package.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pranjal-Prabhat/hand-recognizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
