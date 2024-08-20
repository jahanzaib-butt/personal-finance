# first method

# import random
# import string

# char = string.ascii_letters + string.punctuation + string.digits

# for i in range(12):
#     print(random.choice(char), end="")


# second method

import random
import string


pass_len = 12
# Define the characters to choose from
char = string.ascii_letters + string.punctuation + string.digits

# Generate a 12-character password
# "".join is used to add things between  values
password = "".join([random.choice(char) for i in range(pass_len)])

print(password)
