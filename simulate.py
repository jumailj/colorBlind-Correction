

############################## Color Blindness Simulated ############################################

#simulateColoroptiontitle[SimulatedColorBlindness]
simColorCorrectionTitle = Label(simulateColorBlindness, text="Select Blindness Type:", bg='#868e96', font=('Arial bold', 12))
simColorCorrectionTitle.grid(row=2,column=0)


#current simulating blindness[!imp]
currentSimColorBlindnessValue = IntVar()
currentSimColorBlindnessValue.set("1")


def Choosed(value):
    print('[Log]:option changed ', value)
   


#checkBoxex [SimulatedColorBlindness] 
#Protanopia-checkbox;
simColorCheckBox1 = Radiobutton(simulateColorBlindness, text="Protanopia   " ,command =lambda: Choosed(currentSimColorBlindnessValue.get()), width=18, font=('Arial',12),bg='#868e96', variable = currentSimColorBlindnessValue, value=1)
simColorCheckBox1.grid(row=3,column=0,pady=0)
#Deutranopia-checkbox;
simColorCheckBox2 = Radiobutton(simulateColorBlindness, text="Deutranopia   ",command =lambda: Choosed(currentSimColorBlindnessValue.get()), width=17, font=('Arial',12),bg='#868e96', variable = currentSimColorBlindnessValue, value=2)
simColorCheckBox2.grid(row=3,column=1,pady=0)
#Tritanopia-checkbox;
simColorCheckBox3 = Radiobutton(simulateColorBlindness, text="Tritanopia     ",command =lambda: Choosed(currentSimColorBlindnessValue.get()), width=18,font=('Arial',12),bg='#868e96', variable = currentSimColorBlindnessValue, value=3)
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
chooseImageLabel1 = Label(outputFrame, image =outputImage)
chooseImageLabel1.grid(row=0,column=0)

def GenerateSimImage():
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
    chooseImageLabel1.configure(image=img2)
    chooseImageLabel1.image=img2



#generateSimImageButton[SimulatedColorBlindness]
simulateImageButton = Button(simulateColorBlindness,text="Generate", command=GenerateSimImage, width=15)
simulateImageButton.grid(row=8,pady=10)

