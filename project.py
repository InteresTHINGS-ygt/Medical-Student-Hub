import Medical as med
import Ventor as ven
import Erin as e
import Archetype as ar

print("Welcome to the medical student hub!")
print("This program aims to help medical students with their studies and mental health, and have fun!")

print("Choose an option:")
print("1- Is a medical or healthcare major suitable for you?")
print("2- Erin - Memorizing made fun")
print("3- Ventor - Pipe your negative stuff so it becomes positive")
print("4- Medical Student Archetype Test")

choice = int(input("> ")) # make your choice here

if choice == 1:
    med.med_career()
elif choice == 2:
    e.erin()
elif choice == 3:
    ven.ventor()
elif choice == 4:
    ar.archetype()
else:
    print("You haven't chosen an option. Re-run the program.")