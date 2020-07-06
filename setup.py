from setuptools import Extension, setup, find_packages

try:
    from Cython.Build import cythonize
except ImportError:
    # create closure for deferred import
    def cythonize(*args, ** kwargs):
        from Cython.Build import cythonize
        return cythonize(*args, ** kwargs)

setup(
    name="justatest",
    author='yingshaoxo',
    setup_requires=[
        'cython',
    ],
    ext_modules=cythonize([
        Extension(
            'justatest.hi_library_from_cpp',
            sorted(['c_hi/cython_hi.pyx']),
            include_dirs=[
                # c/cpp defination includes folder path
            ],
            extra_link_args=[],  # like '-lX11'
            language='c++'
        ),
        Extension(
            'justatest.hi_library_from_python',
            sorted(['py_hi/hi.pyx']),
        ),
    ]
    ),
    zip_safe=False,
)
