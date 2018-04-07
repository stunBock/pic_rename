import unittest
from modules.ExifImage import ExifImage
from tests import TestVariables


class ExifImageTest(unittest.TestCase):
    def test_hasDateTimeOriginal_True(self):
        exifImage = ExifImage(TestVariables.exifMaskilImagePath)
        self.assertTrue(exifImage.hasDateTimeOriginal())
        self.assertEqual(exifImage.dateTimeOriginal(), '2015:09:27 18:52:36',
                         'Original date time is {0}'.format(exifImage.dateTimeOriginal()))

    def test_hasDateTimeOriginal_False(self):
        exifImage = ExifImage(TestVariables.testImageList[0])
        self.assertFalse(exifImage.hasDateTimeOriginal())
        self.assertEqual(exifImage.dateTimeOriginal(), '')

    def test_generateName(self):
        exifImage = ExifImage(TestVariables.exifMaskilImagePath)
        self.assertEqual(exifImage.generateName(), '2015_09_27 18_52_36.jpg',
                         'Name is {0}'.format(exifImage.generateName()))

