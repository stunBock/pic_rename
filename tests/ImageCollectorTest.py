import unittest
from modules import ImageCollector
from tests import TestVariables


class ImageCollectorTest(unittest.TestCase):

    def test_count(self):
        self.assertEqual(len(ImageCollector.collect_images_in(TestVariables.testImageDir)),
                         len(TestVariables.testImageList))

    def test_contains(self):
        images = ImageCollector.collect_images_in(TestVariables.testImageDir)
        for image in TestVariables.testImageList:
            self.assertTrue(image in images, '{0} was not found by ImageCollector'.format(image))
