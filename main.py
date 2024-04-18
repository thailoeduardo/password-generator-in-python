import random

print("=============================")
print("Welcome to password gererator")
print("=============================")
print("")

string_de_caracteres = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

input_quantity_of_generated_passwords = input("Amount of password o generate: ")
quantity_of_generated_passwords = int(input_quantity_of_generated_passwords)

input_password_length = input("Enter the length of password: ")
password_length = int(input_password_length)

print("")
print("Here are your passwords: ")

for password in range(quantity_of_generated_passwords):
  generated_passwords = "".join(random.sample(string_de_caracteres, password_length))
  print(generated_passwords)