"""Install setup."""
import setuptools

setuptools.setup(
    name="veoibd_misc",
    version="0.0.1",
    url="git@github.com:ScottSnapperLab/veoibd_misc.git",

    author="Gus Dunn",
    author_email="w.gus.dunn@gmail.com",

    description="A place for random figure creation supporting documentation of the VEOIBD consortium interactions.",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src/python'),


    install_requires=["click",
                      "munch",
                      "seaborn",
                      "pandas",
                      "numexpr",
                      "numpy",
                      "xlrd",
                      "xlwt",
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
