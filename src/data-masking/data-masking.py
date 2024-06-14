import pandas as pd
from faker import Faker

# Rename this field with the name of your file
name_file = "data-in.csv" # Reads data from a .csv or .txt file.

# Create instance Faker
fake = Faker()

# Functions Mask data
def mask_id():
    return fake.random_number(digits=7, fix_len=True)
def mask_name():
    return fake.name()

def mask_last_name():
    return fake.last_name()

def mask_phone_number():
    return fake.phone_number()

# Mask Data
def mask(file):
    file['ID'] = file['ID'].apply(lambda x: mask_id())
    file['Name'] = file['Name'].apply(lambda x: mask_name())
    file['Last Name'] = file['Last Name'].apply(lambda x: mask_last_name())
    file['Phone'] = file['Phone'].apply(lambda x: mask_phone_number())

def outputData(filepath):
    print("---------------output data-----------------", "\n", file.head())

    if filepath.endswith(".csv"):
        file.to_csv('data-out.csv', index=False)
    else:
        file.to_csv('data-out.txt', index=False)


# RUN #
try:
    file = pd.read_csv(name_file)
    print("\n","---------------input data-----------------")
    print(file.head(),"\n")
    mask(file)
    outputData(name_file) # save data

except Exception as ex:
    print("Error when trying to read data",ex)