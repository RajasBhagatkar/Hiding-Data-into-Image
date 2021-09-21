'''FIRST READ THIS BEFORE USE'''
''' 
Image.jpg = Name of the image file 
NeuralNline.py = Name of the file we are going to hide rember the file can be of any type doesn'y matter 
new_file.txt = Name of the New file can be anything

The part that you are going to use just comment out that part😊😊 hope you like it

IMP-NOTE = remember the file extension that you are hiding or if loose it just save in ".txt" format
'''

'''Here we are storing the file inside of an Image'''
# with open("Image.jpg", "ab")  as f, open('NeuralNline.py', 'rb') as p:
# 	f.write(p.read())
# 	print('Sucessful!!')


'''here we are getting the data that we have stored in a image'''
# with open('Image.jpg', 'rb') as f:
# 	content = f.read()
# 	offset = content.index(bytes.fromhex('FFD9'))
#
# 	f.seek(offset + 2)
#
# 	with open('new_file.txt', 'wb') as n:  #creating the new file
# 		n.write(f.read())
# 		print("This is Done writting>>")


