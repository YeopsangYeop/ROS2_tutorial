from setuptools import find_packages, setup

package_name = 'py_topic_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ksy',
    maintainer_email='ksytkdduq03@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'simple_publisher = py_topic_tutorial.simple_publisher:main',
            'simple_subscriber = py_topic_tutorial.simple_subscriber:main',
        ],
    },
)
