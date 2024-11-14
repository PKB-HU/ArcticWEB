from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('content_server_refactored.py', base=base)
]

setup(name='ArcticWEB',
      version = '1.0',
      description = 'ArcticWEB',
      options = {'build_exe': build_options},
      executables = executables)
