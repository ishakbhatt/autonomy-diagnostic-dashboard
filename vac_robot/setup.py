from setuptools import find_packages, setup

package_name = 'vac_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],

    entry_points={
        'console_scripts': [
            'sensor_publisher = vac_robot.main:main'
        ],
    },

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='isha',
    maintainer_email='ishakbhatt25@gmail.com',
    description='Vacuum Robot Publisher',
    license='TODO: License declaration',
)
