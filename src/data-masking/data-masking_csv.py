import pandas as pd
from faker import Faker

try:
    df = pd.read_csv("data-in.csv")
    print(df.head())
except Exception as ex:
    print("Error when trying to read data",ex)

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
df['ID'] = df['ID'].apply(lambda x: mask_id())
df['Name'] = df['Name'].apply(lambda x: mask_name())
df['Last Name'] = df['Last Name'].apply(lambda x: mask_last_name())
df['Phone'] = df['Phone'].apply(lambda x: mask_phone_number())

print(df.head())

#save data
df.to_csv('data-out.csv', index=False)

