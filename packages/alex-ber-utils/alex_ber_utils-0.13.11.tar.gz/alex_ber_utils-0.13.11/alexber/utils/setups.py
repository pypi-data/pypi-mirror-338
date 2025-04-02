import logging
import setuptools
from shutil import rmtree
import os
import sys

logger = logging.getLogger(__name__)

_setup_module = sys.modules['__main__']

_setup_dir = os.path.dirname(os.path.realpath(_setup_module.__file__)) if hasattr(_setup_module, '__file__') \
                                                                        else os.getcwd()
VERSION = getattr(_setup_module, 'VERSION', None)

def _my_rmtree(path, ignore_errors=False, onerror=None):
    try:
        rmtree(path, ignore_errors, onerror)
    except OSError:
        pass

#adapted from https://github.com/kennethreitz/setup.py/blob/master/setup.py
class UploadCommand(setuptools.Command):
    '''
    Support setup.py upload.
    UploadCommand is intented to be used only from setup.py
    It's builds Source and Wheel distribution.
    It's uploads the package to PyPI via Twine.
    It's pushes the git tags.
    '''

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print(f'\033[1m{s}\033[0m')

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status('Removing previous builds...')
        # rm -rf build *.egg-info dist
        _my_rmtree(os.path.join(_setup_dir, 'build'))
        _my_rmtree(os.path.join(_setup_dir, 'f{NAME}.egg-info'))
        _my_rmtree(os.path.join(_setup_dir, 'dist'))

        self.status('Building Source and Wheel distribution...')
        os.system(f'{sys.executable} setup.py sdist bdist_wheel')
        #os.system('python3 setup.py sdist bdist_wheel')

        self.status('Uploading the package to PyPI via Twine...')
        # python -m keyring set https://upload.pypi.org/legacy/ alex-ber
        os.system('twine upload dist/*')

        self.status('Pushing git tags...')
        os.system('git fetch')
        os.system('git commit -m "setup.py changed" setup.py')
        os.system('git push')
        if VERSION is not None:
            os.system(f'git tag v{VERSION}')
            os.system(f'git push origin v{VERSION}')
        #os.system(f'git tag -d v{VERSION}')
        #os.system(f'git push --delete origin v{VERSION}')
        #os.system('git push --tags')

        sys.exit()

class CleanCommand(setuptools.Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for dirpath, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                if filename.endswith(('.pyc', '.pyo', '.pyd')):
                    file_path = os.path.join(dirpath, filename)
                    print(f'Removing {file_path}')
                    os.remove(file_path)
            for dirname in dirnames:
                if dirname == '__pycache__':
                    dir_path = os.path.join(dirpath, dirname)
                    print(f'Removing {dir_path}')
                    _my_rmtree(dir_path)
        _my_rmtree('build', ignore_errors=True)
        _my_rmtree('dist', ignore_errors=True)
        _my_rmtree('*.egg-info', ignore_errors=True)
