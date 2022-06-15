#Control program using if statements
#This type of program is a simple variant of artificial intelligence 
#known as an expert system and the classification tree is known as a decision tree.

print ("Welcome to the Biology Expert")
print ("-----------------------------")
print ("Answer the following questions by selecting from among the options.")

skeleton = input ("The skeleton is (internal/external)?\n")
if skeleton == "internal":
   fertilisation = input ("The fertilisation of eggs occurs (within the body/outside the body)?\n")
   if fertilisation == "within the body":
      young = input ("Young are produced by (waterproof eggs/live birth)?\n")
      if young == "waterproof eggs":
         skin = input ("The skin is covered by (scales/feathers)?\n")
         if skin == "scales":
            print ("Type of animal: Reptile")
         else:
            print ("Type of animal: Bird")
      else:
         print ("Type of animal: Mammal")
   else:
      lives = input ("It lives (in water/near water)?\n")
      if lives == "in water":      
         print ("Type of animal: Fish")
      else:   
         print ("Type of animal: Amphibian")
else:
   print ("Type of animal: Arthropod")
   