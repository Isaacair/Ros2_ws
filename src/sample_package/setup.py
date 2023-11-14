from setuptools import setup
import os

package_name = 'sample_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        ('share/' + package_name + '/models', [os.path.join('models', f) for f in os.listdir('models') if f.endswith('.pkl')]),
    ],
    install_requires=['setuptools','sklearn'],
    zip_safe=True,
    maintainer='tony_stark',
    maintainer_email='tony_stark@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    

    entry_points={
        'console_scripts': [
        "talk=sample_package.talker_nod:main",
        "senpub=sample_package.sensor_publish:main",
        "process=sample_package.processing:main",
        "fan_sub=sample_package.fan_subscriber:main"
        ],
    },
)
