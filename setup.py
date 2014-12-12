from cx_Freeze import setup, Executable

includefiles = ['resources\map.txt']
includes = []
excludes = []
packages = []

setup(
    name = 'Adventure',
    version = '1.0.0',
    description = 'A nice little text based adventure game.',
    author = 'Trevor Valcourt',
    author_email = 'tjvalcourt@wpi.edu',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('game.py')]
)
