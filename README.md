# Make-any-QR-Code-using-Python
-> What is a QR code?

Basically, a QR code works in the same way as a barcode at the supermarket. Quite simply, a QR code is an encoded piece of data. The data in a QR code can be alphanumeric, numeric, or binary. Although that is the technical explanation of how a QR code works, something much more important to focus on is the fact that QR codes can be scanned at the touch of a button by the hundreds of millions of people around the world that use a Smartphone on a daily basis. This makes them great for marketers. This makes QR codes an extremely simple way to access stored information in an instant which in turn, makes them a perfect solution to conversion-hungry marketers.

-> Setup:-

first, open your IDE like VS code or Pycharm for starting the project download this package for the project in terminal

     pip install qrcode
then import the package to use it

->for beginner level:-

    import qrcode
    image=qrcode.make("https://github.com/suyashftr")   #here I have inserted the link for which I'm making QR code
    image.save("Github.png")                            #here is the name for your Qr code 
->for Adavance level :-

    import qrcode
    from PIL import Image

    qr=qrcode.QRCode(version=1,
             error_correction=qrcode.constants.ERROR_CORRECT_H ,
             box_size=10, border=4,)
    qr.add_data("https://github.com/suyashftr")
    qr.make(fit=True)
    image=qr.make_image(fill_color="blue",background_color="white")
    image.save("linkedIn_colourful.png")
    
Here we used are qrcode package by giving it a version=1 the version parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix).

error_correction 
-> used which have different slots of low level, medium level, medium-high level (Q), and higher level error. we have used "ERROR_CORRECT_H" higher level error_correction.

    ERROR_CORRECT_L
About 7% or less errors can be corrected.

    ERROR_CORRECT_M (default)
About 15% or less errors can be corrected.

    ERROR_CORRECT_Q
About 25% or less errors can be corrected.

    ERROR_CORRECT_H.
About 30% or less errors can be corrected.

qr.add_data 
-> used for adding a link to my Github profile you can add your website link or any other link to create your own Qr code.

qr.make  
-> used for making QRcode using the package qrcode this method forwards additional keyword arguments to the underlying ElementTree XML library.

image.save
-> The module also provides a number of factory functions, including functions to load images from files, and to create new images. Saves this image under the given filename.

output:-


![linkedIn_colourful](https://github.com/suyashstr/Make-any-QR-Code-using-Python/assets/141958076/9cb476b4-99b0-499e-9f80-edb1360ff613) ![linkedIn_diff_cases2](https://github.com/suyashstr/Make-any-QR-Code-using-Python/assets/141958076/0ada9ff3-3e41-44f2-851a-ea0af2c3ce5b)

![LinkdeIn black   white](https://github.com/suyashstr/Make-any-QR-Code-using-Python/assets/141958076/b29fa50a-9457-46f7-956d-237def8eebb7)

![linkedIn_colour](https://github.com/suyashstr/Make-any-QR-Code-using-Python/assets/141958076/22ebf419-f310-40ce-ac37-11518b8140fb)

![linkedIn_diff_cases](https://github.com/suyashstr/Make-any-QR-Code-using-Python/assets/141958076/7c19a3e8-2f23-46db-a7ff-218229cfb842)
