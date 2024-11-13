from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('Stray.py', base=base)
]

setup(name='Stray',
      version = '1.0',
      description = 'Stray Client',
      options = {'build_exe': build_options},
      executables = executables)
