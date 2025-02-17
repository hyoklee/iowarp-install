from spack import *

class PpiChiNettest(CMakePackage):
    homepage = "https://github.com/lukemartinlogan/ppi-chi-nettest.git"
    git = "https://github.com/lukemartinlogan/chi-nettest.git"
    version('main', branch='main', submodules=True)
    
    # Required deps
    # depends_on('cte-hermes-shm@2: +mochi -nocompile', type=('build'))
    depends_on('catch2@3.0.1')
    depends_on('yaml-cpp')
    depends_on('doxygen')
    depends_on('mochi-thallium+cereal@0.10.1')
    depends_on('argobots@1.1+affinity')
    depends_on('cereal')

    def cmake_args(self):
        args = []
        return args