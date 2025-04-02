from setuptools import setup, find_packages

setup(
    name='dev-laiser',
    version='0.2.19', 
    author='Satya Phanindra Kumar Kalaga, Bharat Khandelwal, Prudhvi Chekuri', 
    author_email='phanindra.connect@gmail.com',  
    description='LAiSER (Leveraging Artificial Intelligence for Skill Extraction & Research) is a tool designed to help learners, educators, and employers extract and share trusted information about skills. It uses a fine-tuned language model to extract raw skill keywords from text, then aligns them with a predefined taxonomy. You can find more technical details in the project’s paper.md and an overview in the README.md.', 
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://github.com/LAiSER-Software/extract-module',  
    packages=find_packages(),  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy==1.26.4',
        'pandas==2.2.2',
        'psutil==5.9.8',
        'skillNer==1.0.3',
        'scikit-learn==1.5.1',
        'spacy==3.7.4',
        'tokenizers==0.13.3',
        'accelerate==0.27.1',
        'bitsandbytes==0.43.1',
        'datasets==2.20.0',
        'huggingface_hub==0.23.4',
        'peft==0.11.1',
        'torch==2.3.1',
        'trl==0.9.4',
        'ipython==8.27.0',
        'python-dotenv',
        'vllm',
        'tqdm',
        'triton'
    ],

)