from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from recolor import Core

#preview image widht and height;
PreviewImageWidht=370
previewImageHeight=205

outputImageWidht = 1258
outputImageHeight= 795


window = Tk() #create new window;
window.title('Color-Blindness') #window title;
window.geometry('1640x820') #window size locked;
window.configure(bg='#495057') # window background color;
window.resizable(False,False) #windows can't resize

#preivew image [default]
img = ImageTk.PhotoImage(Image.open('default_out.jpg').resize((PreviewImageWidht,previewImageHeight)))

#preview Output Image[Default]
outputImage = ImageTk.PhotoImage(Image.open('default_out.jpg').resize((outputImageWidht,outputImageHeight)))


frame = Frame(window) #create and define;
frame.pack() #pack /place /grid -->layout managers;

#1 row and #2 column,

#leftSide Setting Frame [column -1]
settingsFrame = LabelFrame(frame, text="⚙SETTINGS", font=('Arial',13), borderwidth = 0,highlightthickness =0 , bg='#868e96')
settingsFrame.grid(row=0, column=0, padx=0, pady=0) 


#rightSide Output Frame [column -2]
outputFrame = LabelFrame(frame,text="OUTPUT", font=('Arial',13), borderwidth = 0,highlightthickness =0 ,bg='#495057')
outputFrame.grid(row=0, column=1)

#leftSide-1-imageSettings-Frame [ column-1 , row -1]
imageSettingsFrame = LabelFrame(settingsFrame, text="Image Settings", font=('Arial',13),bg='#868e96')
imageSettingsFrame.grid(row=0, column=0, padx=0, pady=0) 

#leftSide-1-simulateColorblindness-Frame [ column -1, row-2]
simulateColorBlindness = LabelFrame(settingsFrame, text="Simulate Color Blindness",font=('Arial',13),bg='#868e96')
simulateColorBlindness.grid(row=1, column=0, padx=0, pady=0) 


#leftSide-1-colorCorrection-Frame [ column -1, ]
colorCorrectionFrame = LabelFrame(settingsFrame, text="Color Correction", font=('Arial',13),bg='#868e96')
colorCorrectionFrame.grid(row=2, column=0, padx=0, pady=0) 


# Select Image and Update to Preview Box;
def GetImageFile():
    print('[Log]: Image Button pressed')
 
    window.filename = filedialog.askopenfilename(initialdir="/gui/images", title="select a File")
    #todo error handling, when user didn't choose any files.

    #change current image dir to user defined.
    CurrentImageDir =  window.filename
    #update new image with help of filepath
    img2 = ImageTk.PhotoImage(Image.open(window.filename).resize((PreviewImageWidht,previewImageHeight)))
    print('[Log]: (file path) :' + CurrentImageDir )

    #write the dir to a file
    f = open('dir.txt', 'a')
    f.truncate(0)
    f.write(CurrentImageDir)
    f.close()

    #replace image default image with updated image;
    previewImage.configure(image=img2)
    previewImage.image=img2


# ChooseImageButton  [settingsframe]
chooseImageLabel = Button(imageSettingsFrame, text="Choose Image📁", command =GetImageFile, height= 1, width=40)
chooseImageLabel.grid(row=0,column=0)

#preview_image [SettingsFrame]
previewImage = Label(imageSettingsFrame, image=img)
previewImage.grid(row=1,column=0, pady=4)

#### code of simulation ################ <<<

############################## Color Blindness Simulated ############################################

#simulateColoroptiontitle[SimulatedColorBlindness]
simColorCorrectionTitle = Label(simulateColorBlindness, text="Select Blindness Type:", bg='#868e96', font=('Arial bold', 12))
simColorCorrectionTitle.grid(row=2,column=0)


#current simulating blindness[!imp]
currentSimColorBlindnessValue = IntVar()
currentSimColorBlindnessValue.set("1")


def SimChoosed(value):
    print('[Log]:option changed ', value)
   

#checkBoxex [SimulatedColorBlindness] 
#Protanopia-checkbox;
simColorCheckBox1 = Radiobutton(simulateColorBlindness, text="Protanopia   " ,command =lambda: SimChoosed(currentSimColorBlindnessValue.get()), width=18, font=('Arial',12),bg='#868e96', variable = currentSimColorBlindnessValue, value=1)
simColorCheckBox1.grid(row=3,column=0,pady=0)
#Deutranopia-checkbox;
simColorCheckBox2 = Radiobutton(simulateColorBlindness, text="Deutranopia   ",command =lambda: SimChoosed(currentSimColorBlindnessValue.get()), width=17, font=('Arial',12),bg='#868e96', variable = currentSimColorBlindnessValue, value=2)
simColorCheckBox2.grid(row=3,column=1,pady=0)
#Tritanopia-checkbox;
simColorCheckBox3 = Radiobutton(simulateColorBlindness, text="Tritanopia     ",command =lambda: SimChoosed(currentSimColorBlindnessValue.get()), width=18,font=('Arial',12),bg='#868e96', variable = currentSimColorBlindnessValue, value=3)
simColorCheckBox3.grid(row=4,column=0,pady=6)


#simulateColorDegreeValueTitle[SimulatedColorBlindness]
simDegreeValueTitle = Label(simulateColorBlindness, text="Choose Degree Value:", bg='#868e96', font=('Arial bold', 12))
simDegreeValueTitle.grid(row=5, column=0)


#simulateColorDegreeSlider[SimulatedColorBlindness]
degreeSlider = Scale(simulateColorBlindness,sliderlength = 10, from_=-0, to=10.0, orient =HORIZONTAL, bg='#868e96',borderwidth=0,highlightthickness= 0, width=14)
degreeSlider.grid(row=6)

# to get the slider value; degreeSlider.get()


#generateSimImageTitle[SimulatedColorBlindness]
generateSimulateImageTitle = Label(simulateColorBlindness, text="Simulate Image:            ", bg='#868e96', font=('Arial bold', 12))
generateSimulateImageTitle.grid(row=7, column=0,pady=10)


#OutPutImage [OutputFrame]
chooseImageLabel = Label(outputFrame, image =outputImage)
chooseImageLabel.grid(row=0,column=0)


def GenerateSimulateImage():
    print('------------------------------')
    print('[Log] sim Button pressed')
    f = open("dir.txt", 'r')
    value = f.read()
    print('[Log] Image dir:', value)
    print('[Log] Choosed Blindness: ', currentSimColorBlindnessValue.get())
    print('[Log] Degree Value: ', degreeSlider.get())

    DegreeValue = degreeSlider.get()

    simColorValue_ = 'protanopia'
    simColorValue = currentSimColorBlindnessValue.get()
    
    if simColorValue == 1:
        simColorValue_ = 'protanopia'
        print('option 1 is selected and its protanopia')
    elif  simColorValue == 2:
        simColorValue_ = 'deutranopia'
        print('option 2 is selected and its deutranopia')
    elif  simColorValue == 3:
        simColorValue_ = 'tritanopia'
        print('option 3 is selected and its tritanopia')

    print('    [ degree ]  :', DegreeValue*0.1)

    # add algorithm and generate image;
    Core.simulate(input_path = value,return_type= 'save',save_path='out.jpg',simulate_type= simColorValue_,simulate_degree_primary=DegreeValue*0.1)


    #update new image with help of filepath
    img2 = ImageTk.PhotoImage(Image.open('out.jpg').resize((outputImageWidht,outputImageHeight)))

    #todo apply algorithm to process image; :)

    #replace image default image with updated image;
    chooseImageLabel.configure(image=img2)
    chooseImageLabel.image=img2


#generateSimImageButton[SimulatedColorBlindness]
simulateImageButton = Button(simulateColorBlindness,text="Generate", command=GenerateSimulateImage, width=15)
simulateImageButton.grid(row=8,pady=10)



######################################## color Correction #####################################################

#Coloroptiontitle[ColorBlindness]
ColorCorrectionTitle = Label(colorCorrectionFrame, text="Select Blindness Type:", bg='#868e96', font=('Arial bold', 12))
ColorCorrectionTitle.grid(row=0,column=0)


#current simulating blindness[!imp]
currentColorCorrectionValue = IntVar()
currentColorCorrectionValue.set("1")


def ChoosedCorrection(value):
    print('[Log]:option changed ', value)
   

#checkBoxex [SimulatedColorBlindness] 
#Protanopia-checkbox;
ColorCorrectionCheckBox1 = Radiobutton(colorCorrectionFrame, text="Protanopia   " ,command =lambda: ChoosedCorrection(currentColorCorrectionValue.get()), width=18, font=('Arial',12),bg='#868e96', variable = currentColorCorrectionValue, value=1)
ColorCorrectionCheckBox1.grid(row=1,column=0,pady=0)
#Deutranopia-checkbox;
ColorCorrectionCheckBox2 = Radiobutton(colorCorrectionFrame, text="Deutranopia   ",command =lambda: ChoosedCorrection(currentColorCorrectionValue.get()), width=17, font=('Arial',12),bg='#868e96', variable = currentColorCorrectionValue, value=2)
ColorCorrectionCheckBox2.grid(row=1,column=1,pady=0)
#Tritanopia-checkbox;
ColorCorrectionCheckBox3 = Radiobutton(colorCorrectionFrame, text="Tritanopia     ",command =lambda: ChoosedCorrection(currentColorCorrectionValue.get()), width=18,font=('Arial',12),bg='#868e96', variable = currentColorCorrectionValue, value=3)
ColorCorrectionCheckBox3.grid(row=2,column=0,pady=6)



#simulateColorDegreeValueTitle[SimulatedColorBlindness]
CorrectionDegreeValueTitle = Label(colorCorrectionFrame, text="Choose Degree Value:", bg='#868e96', font=('Arial bold', 12))
CorrectionDegreeValueTitle.grid(row=3, column=0)


#simulateColorDegreeSlider[SimulatedColorBlindness]
CorrectionDegreeSlider = Scale(colorCorrectionFrame,sliderlength = 10, from_=-0, to=10.0, orient =HORIZONTAL, bg='#868e96',borderwidth=0,highlightthickness= 0, width=14)
CorrectionDegreeSlider.grid(row=4)



#generateSimImageTitle[SimulatedColorBlindness]
generateCrtImageTitle = Label(colorCorrectionFrame, text="Correct Image:            ", bg='#868e96', font=('Arial bold', 12))
generateCrtImageTitle.grid(row=5, column=0,pady=10)


def GenerateCorrectImage():
    print('------------------------------')
    print('[Log] sim Button pressed')
    f = open("dir.txt", 'r')
    value = f.read()
    print('[Log] Image dir:', value)
    print('[Log] Choosed Blindness: ', currentColorCorrectionValue.get())
    print('[Log] Degree Value: ', CorrectionDegreeSlider.get())

    crtDegreeValue = CorrectionDegreeSlider.get()

    crtColorValue_ = 'protanopia'
    crtColorValue = currentColorCorrectionValue.get()
    
    if crtColorValue == 1:
        crtColorValue_ = 'protanopia'
        print('option 1 is selected and its protanopia')
    elif  crtColorValue == 2:
        crtColorValue_ = 'deutranopia'
        print('option 2 is selected and its deutranopia')
    elif  crtColorValue == 3:
        crtColorValue_ = 'tritanopia'
        print('option 3 is selected and its tritanopia')

    print('    [ degree ]  :', crtDegreeValue*0.1)

    # add algorithm and generate image;
    Core.simulate(input_path = value,return_type= 'save',save_path='out.jpg',simulate_type= crtColorValue_,simulate_degree_primary=crtDegreeValue*0.1)


    #update new image with help of filepath
    img2 = ImageTk.PhotoImage(Image.open('out.jpg').resize((outputImageWidht,outputImageHeight)))

    #todo apply algorithm to process image; :)

    #replace image default image with updated image;
    chooseImageLabel.configure(image=img2)
    chooseImageLabel.image=img2


#generateSimImageButton[SimulatedColorBlindness]
correctImageButton = Button(colorCorrectionFrame,text="Generate", command=GenerateCorrectImage, width=15) # changed, function
correctImageButton.grid(row=6,pady=10)

#todos add  image compression; - sugg.


# start window;
window.mainloop()