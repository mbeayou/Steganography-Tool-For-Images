# Simple Steganography Tool
Steganography is the practice of hiding data in plain sight. Steganography is often embedded in images or audio.

## Preview:
![alt text](https://github.com/mbeayou/Steganography-Tool-For-Images/raw/master/src/assits/home.png)
![alt text](https://github.com/mbeayou/Steganography-Tool-For-Images/raw/master/src/assits/hide1.png)
![alt text](https://github.com/mbeayou/Steganography-Tool-For-Images/raw/master/src/assits/hide2.png)
![alt text](https://github.com/mbeayou/Steganography-Tool-For-Images/raw/master/src/assits/reveal1.png)
![alt text](https://github.com/mbeayou/Steganography-Tool-For-Images/raw/master/src/assits/reveal2.png)

## LSB Method:
he LSB (Least Significant Bit) method is one of the simplest and most commonly used techniques in steganography. It involves replacing the least significant bit of each byte in an image, audio file, or other digital media with a bit of the secret message. Since the least significant bit contributes the least to the overall value of the byte, altering it slightly typically does not noticeably change the appearance or quality of the medium to the human eye or ear.

1-  In digital images, each pixel is represented by a combination of red, green, and blue (RGB) color values. Each color value typically occupies 8 bits (1 byte), ranging from 0 to 255.

2- the LSB of each color value can be manipulated to encode a single bit of the secret message. Since the LSB contributes the least to the overall color value, altering it slightly has minimal impact on the appearance of the pixel.

Example: Suppose we have an image pixel with the following RGB values:

    Red: 11001100
    Green: 10101010
    Blue: 11110000

To hide a binary message "101" using the LSB method:

    We replace the LSB of each color value with a bit of the message:
        Red: 11001101
        Green: 10101010
        Blue: 11110001
## Refernces 
https://ctf101.org/forensics/what-is-stegonagraphy/  

https://www.geeksforgeeks.org/image-based-steganography-using-python/