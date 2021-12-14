NAME=input("What is your name? :")
height_cm=input("What is your height in centimetres?(Number only e.g. 150) :")
#1 cm is equal to 1/2.54 inches, 12 inches in a foot
height_in=int(height_cm)/2.54
F=int(height_in//12)
I=int(height_in%12)
Q=int(4*(height_in-F*12-I))

print("Dear", NAME.upper(), "you are", F ,"feet", I, Q,"/4 inches tall.")
input("Press enter to exit")

