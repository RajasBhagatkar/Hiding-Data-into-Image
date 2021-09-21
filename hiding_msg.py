''' FIRST READ BEFORE USE '''
'''
here we are trying to hide the message that we wnat to enter in to an Image
why we can do that :- we know that every image start's with :-FFD8FF  end's with:-FFD9
they stop readind at the end when they hit "FFD9"

imp-Note:- comment-out the part that you want to use for ease i have commented all the part
 Image.jpg == Name of the Image
 '''

'''writting into an Image'''
# with open("Image.jpg", 'ab') as f:
#     f.write(b'Hello World!!')   #type msg



'''Reading from an Image'''
# with open("Image.jpg", 'rb') as f:
#     content = f.read()
#     offset = content.index(bytes.fromhex("FFD9"))
#     # here we are going two bytes futber becuz FF=one byte and D9=second byte of Index
#     f.seek(offset + 2)
#     print(f.read())


'''This is to remove the information stored on Image'''
# rember that "rb+" for both reading and appending in binary
# with open("Image.jpg", 'rb+') as f:
#     content = f.read()
#     offset = content.index(bytes.fromhex("FFD9"))
#     pointer = f.seek(offset + 2)
#
#     # truncate remove everything from that index which we give it
#     f.truncate(pointer)
#     print(f.read())