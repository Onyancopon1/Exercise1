def corrector(question_text):

      while True:

            answer = input(question_text).lower()

            if answer == "residential" or answer == "r":
                  answer="Residential"
                  return answer

            elif answer=="commercial" or answer =="c":
                  answer="Commercial"
                  return answer

            else:
                  print("Please enter full word or first letter")


def calculator(height,length):
      if rorc=="Residential":
            vol1=height*length*0.25
            return vol1
      elif rorc=="Commercial":
            vol2=height*length*0.5
            return vol2
      else:
            print("Please enter number only")


rorc = corrector("Residential(R) or Commercial(C):")

print(f"\n"
      f"Your building is {rorc}")

height=int(input("\n"
                 "Type height of the building in meters:"))
length=int(input("\n"
                 "Type length of the building in meters:"))
volume=calculator(height,length)

print(f"Your volume of the foundation is {volume}m^3")






