from setuptools import setup, Extension

mojo_arrow_sys_module = Extension(
    'mojo_arrow_sys',
    sources=['mojo_arrow_sys/mojo_arrow_sys.c'],
    include_dirs=[],
    libraries=[],
    extra_compile_args=['-Wall', '-Wextra']
)

setup(
    name='mojo_arrow_sys',
    version='0.1.0',
    description='Python C extension for accessing Arrow C streams from Mojo',
    author='Mihai Seritan',
    author_email='mihai.seritan@example.com',
    url='https://github.com/mseritan/mojo_arrow_sys',
    ext_modules=[mojo_arrow_sys_module],
    python_requires='>=3.7',
)