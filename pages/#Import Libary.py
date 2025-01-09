import qrcode
from qrcode.image.pure import PyPNGImage
img = qrcode.make('Some data here', image_factory=PyPNGImage)