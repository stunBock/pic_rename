import os

testDir = os.path.join(os.getcwd(), 'tests')
resourceDir = os.path.join(testDir, 'resources')
testImageDir = os.path.join(resourceDir, 'testImages')


def generateFullPathForImage(imageName):
    imageWithPath = testImageDir
    for part in imageName.split('/'):
        imageWithPath = os.path.join(imageWithPath, part)
    return imageWithPath

exifMaskilImagePath = generateFullPathForImage('exif_maskil.JPG')

testImageList = [generateFullPathForImage('cross.jpg'),
                 generateFullPathForImage('cross_png.png'),
                 generateFullPathForImage('mountain_png.png'),
                 generateFullPathForImage('mountain.jpeg'),
                 generateFullPathForImage('subdir/subdir_cross.jpg'),
                 generateFullPathForImage('subdir/subdir_cross_png.png'),
                 generateFullPathForImage('subdir/subdir_mountain.jpeg'),
                 generateFullPathForImage('subdir/subdir_mountain_png.png'),
                 exifMaskilImagePath]
