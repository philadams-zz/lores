from fabric.api import local


def d_register():
    local('python setup.py register')

def d_prepare():
    local('python setup.py sdist')

def d_distribute():
    local('python setup.py sdist upload')
