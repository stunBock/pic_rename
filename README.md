# pic_rename
this program will go through your library of pictures and rename them according to the EXIF-Data. 
If there is no Exif Data pictures will not be renamed. If there are Files that aren't JPG or  PNG they will be ignored ... (this could be added)
You just start the script in any directory and it will search within all subdirectories. it will tell you how many pictures it found
and ask you before processing. 

## Dev Setup

### Python 3.4

The module `exifread` needs python 3.4 or lower.

#### OS X
- `brew install pyenv`
- `pyenv install 3.4.8`
- add to `/Users/YOUR_USERNAME/.bash_profile`
  ```
  export PATH="/Users/YOUR_USER_NAME/.pyenv:$PATH"
  eval "$(pyenv init -)"
  ```
- `pyenv local 3.4.8` or `pyenv global 3.4.8`

Install directory will be `/Users/YOUR_USER_NAME/.pyenv/versions/3.4.8`.

To check if the right version is used run `python -V`.

### EXIF_READ
Install Exifread module:
``pip install exifread``

For more information s. https://pypi.python.org/pypi/ExifRead

## Run tests
`python -m unittest discover tests -p "*Test.py"`

For `unittest` documentation s. https://docs.python.org/3/library/unittest.html

# License

This program is under the MIT license.

## Images

All images not starting with _"exif"_ are taken from https://www.pexels.com and are under the CC0 license:
- Free for personal and commercial use
- No attribution required

All other images are privately taken and hereby granted permission to everyone to use them according to CC0.