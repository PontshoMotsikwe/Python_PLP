def modify_content(content):
    return content.upper()

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as infile:
        content = infile.read()
    
    modified_content = modify_content(content)
    
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)
    
    print(f"Modified content written to '{new_filename}' successfully!")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' could not be read or written.")
