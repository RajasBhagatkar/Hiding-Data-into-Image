# Hiding-Data-into-Image

## Here we are able to Hide Fully Executable file or message without changeing the Image or Image functionality 
# About:
In order to see why we can do that How we can do that we First have to look into an bytes of the jpeg file to see the byte information of Image we have to use an Hex-Editor such as "Hex Editor Neo" 
When we open an Image in Hex-Editor we are going to see an special thing that all the Image byte start with the sequence "FFD8FF' and they all end's with the squence "FFD9"

![image](https://user-images.githubusercontent.com/89124523/134191315-b49b6673-478e-42d2-9e4b-01fb8806af9c.png)

![image](https://user-images.githubusercontent.com/89124523/134191472-23bdd04e-498e-469f-9af1-5cd8b931ad82.png)

So any thhing that we enter after the "FFD9" sequece does not matter becuz this basically means that they should stop at this point 
