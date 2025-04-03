from setuptools import setup, find_packages

setup(
    name="grading_package",
    version="0.1.3",
    description="A brief description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Elton Morden, Joyce Elli, Jefferson Forson, Joseph Agyemang, Lovelace John Kwaku Baidoo, Claude Osabu-Kle",
    author_email="eltonmorden029@gmail.com, lovelacejohnkwakubaidoo@gmail.com, claude.osabu-kle@st.rmu.edu.gh, joseph.agyemang@st.rmu.edu.gh, joyce.elli@st.rmu.edu.gh, jefferson.forson@st.rmu.edu.gh",
    url="https://github.com/Elton133/GRADING-PACKAGE",
    packages=find_packages(),
    install_requires=[
        # List any dependencies here, e.g.,
        # 'numpy', 'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
