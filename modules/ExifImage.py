import exifread

DATE_TIME_ORIGINAL = 'EXIF DateTimeOriginal'


class ExifImage:
    def __init__(self, imagePath):
        self.image = open(imagePath, "rb")
        self.exifInfo = exifread.process_file(self.image)

    def dateTimeOriginal(self):
        if self.hasDateTimeOriginal():
            return str(self.exifInfo[DATE_TIME_ORIGINAL])
        return ''

    def hasDateTimeOriginal(self):
        return (DATE_TIME_ORIGINAL in self.exifInfo.keys()) and (self.exifInfo[DATE_TIME_ORIGINAL] != '')

    def generateName(self):
        return self.dateTimeOriginal().replace(':', '_') + '.' + self._getFileType()

    def _getFileType(self):
        return self.image.name.rsplit('.', 1)[1].lower()

    def __del__(self):
        self.image.close()
