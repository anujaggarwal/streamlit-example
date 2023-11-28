# import altair as alt
# import numpy as np
# import pandas as pd
import streamlit as st
import re

res = [60, 80, 70, 30, 90, 20, 100, 40, 50]

def remove_special_characters_and_spaces(input_string):
    # Remove special characters using regex
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)

    # Remove white spaces
    cleaned_string = cleaned_string.replace(" ", "")
    print(cleaned_string)

    return cleaned_string

# # Example usage:
# original_string = "Hello, World! 123"
# result = remove_special_characters_and_spaces(original_string)
# print(result)

def ascii_equivalent_case_insensitive(input_string):
    total_ascii = 0
    for char in remove_special_characters_and_spaces(input_string):
        total_ascii += (ord(char.lower()) - 96)  # Convert each character to lowercase before getting the ASCII value
    return (total_ascii % 9) if (total_ascii % 9) else 9

"""
# Welcome !!!

Please enter name of your child or your company which you want us to suggest.
"""

name = st.text_input('Name')
st.write('Name: ', name)
# st.write('Value: ', ascii_equivalent_case_insensitive(name))
st.write('Value: ', res[ascii_equivalent_case_insensitive(name) - 1], ' / 100')



# Example usage:
# print(ascii_equivalent_case_insensitive("krishyam technologies private limited"))


