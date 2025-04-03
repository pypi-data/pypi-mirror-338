from setuptools import setup, find_packages

setup(
    name="easycnnpro",
    version="1.0.0",
    description="EasyCnnPro: Intuitive Python library for creating, training and visualizing convolutional neural networks. Features simplified CNN layer definition, automated training workflows, model visualization, and seamless Keras-to-ONNX conversion. Includes 15 pre-configured popular models for immediate use.",
    packages=find_packages(),
    author="Gabriel Wiśniewski",
    author_email="gabrys.wisniewski@op.pl",
    classifiers=[  
        "Programming Language :: Python :: 3",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent", 
    ],
     install_requires=[
        "tensorflow",
        "numpy",
        "matplotlib",
        "opencv-python",
        "tf2onnx",
        "onnx"
    ],
    entry_points={
        "console_scripts":[
            "easycnn-core = easycnn:EasyCNN",
            "easycnn-preset = easycnn:Preset",
            "easycnn-visualizer = easycnn:TrainingVisualizer",
            "easycnn-exporter = easycnn:EasyExporter",
            
        ]
    }
)