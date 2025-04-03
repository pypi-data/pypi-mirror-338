from setuptools import setup, find_packages

setup(
    name='sgx-storage-client',
    version='0.0.1',
    description='sgx storage client',
    author='Maksim',
    author_email='mpe@exan.tech',
    include_package_data=True,
    install_requires=[
        'requests==2.32.3',
        'cryptography==44.0.2',
        'pycryptodome==3.22.0',
    ],
    python_requires='>=3.8',
    license='EULA',
    zip_safe=False,
    keywords='sgx security enclave dcap attestation',
    packages=find_packages(exclude=['docs', 'tests']),
)
