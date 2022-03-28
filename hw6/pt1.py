from matplotlib.image import imread
import matplotlib.pyplot as plt
import time

class Image:
    def __init__(self, path, load_time):
        self.img = imread(path)
        self.load_time = load_time
        self.proxy = ImageProxy()
        
    def show_image(self):
        self.proxy.check_and_placehold(load_time=self.load_time, img=self.img)
        

class ImageProxy:
    def __init__(self):
        self.wait_time = 2
        self.placeholder = imread("hw6/placeholder.png")
    
    
    def check_and_placehold(self, load_time, img):
        if load_time>self.wait_time:
            print("Showing placeholder as it takes time to load.")
            plt.imshow(self.placeholder)
            plt.show()
            time.sleep(load_time)
            plt.imshow(img)
            plt.show()
        else:
            print("Showing the image, no much time to load. Putin takes no time.")
            time.sleep(load_time)
            plt.imshow(img)
            plt.show()
        
    

putin_path = 'hw6/putin.jpeg'
zelensky_path = 'hw6/zelensky.jpg'
load_time = 5

user1 = Image(path=zelensky_path, load_time=5)
user2 = Image(path=putin_path, load_time=1)

user1.show_image()

user2.show_image()