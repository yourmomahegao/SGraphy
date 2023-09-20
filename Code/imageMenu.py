import os
from PIL import Image
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from encryption import Encryptor

class ImageMenu():
    def __init__(self, ProgramUI):
        super(ImageMenu, self).__init__()

        # Initalizing program ui
        self.currentImagePath = None
        self.pui = ProgramUI

    def encryptImage(self):
        # Checking current image path
        if not self.currentImagePath:
            return
        
        # Encrypting current image
        key = self.enc.encrypt(self.currentImagePath, self.pui.ui.textToEncode.text())
        self.pui.ui.textToEncode.setText('')
        self.pui.ui.secretKey.setText(key)

    def decryptImage(self):
        # Checking current image path
        if not self.currentImagePath:
            return
        
        # Getting text from current image
        text = self.enc.decrypt(self.currentImagePath, self.pui.ui.secretKey.text())

        # Trying to decrypt file
        if text is False:
            self.pui.ui.secretKeyHelpLabel.setText('Не удалось расшифровать файл!')
        else:
            self.pui.ui.textToEncode.setText(text)


    def initialize(self):
        self.addDragAndDrop()
        self.pui.ui.addImageButton.clicked.connect(self.openImageFileDialog)

        self.pui.ui.imagesList.itemClicked.connect(self.chooseImageHandler)

        # Initializing encryptor
        self.enc = Encryptor()
        self.pui.ui.encryptButton.clicked.connect(self.encryptImage)
        self.pui.ui.decryptButton.clicked.connect(self.decryptImage)

    def openImageFileDialog(self):
        path = QFileDialog.getOpenFileName(self.pui.ui.addImageButton, 'Открыть файл', '',
                                        'All Files (*.*)')
        if path != ('', ''):
            self.pui.ui.imagesList.addItem(path[0])

    def addDragAndDrop(self):
        # Adding drag and drop
        self.pui.ui.imageDropbox.dragEnterEvent = self.imageDropboxEnterEvent
        self.pui.ui.imageDropbox.dropEvent = self.imageDropboxDropEvent

    def chooseImageHandler(self, item):
        # Getting the image
        self.currentImagePath = item.text()

        # Setting image preview
        self.pui.ui.imagePreview.setPixmap(QPixmap(self.currentImagePath))

        # Setting preview values
        imageSize = round(os.path.getsize(self.currentImagePath) / 1024, 2)
        self.pui.ui.imageSizeText.setText(f"Размер: {imageSize} КБайт")

        imagePIL = Image.open(self.currentImagePath)
        self.pui.ui.imageWidthText.setText(f"Ширина: {imagePIL.width} пикселей")
        self.pui.ui.imageHeightText.setText(f"Высота: {imagePIL.height} пикселей")


    def imageDropboxEnterEvent(self, event):
        # Getting mime data
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def imageDropboxDropEvent(self, event):
        # Getting files urls from mime data
        files = [u.toLocalFile() for u in event.mimeData().urls()]

        # Adding files to dropbox
        for f in files:
            self.pui.ui.imagesList.addItem(f)