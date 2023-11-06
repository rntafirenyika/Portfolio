"""
Prompts the user for the name of a file and then outputs that file's media type if the file's name ends,
case-insensitively, in any of these suffixes: .gif .jpg .jpeg .png .pdf .txt .zip
If the file's name ends with some other suffix or has no suffix at all,
output application/octet-stream instead, which is a common default.
"""

def main():
    #Prompt the user for the file name with extension
    filename = formatans(input("Please enter the file name including the extension. \n"))

    #Checks the file extension and outputs the media type
    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".txt"):
        print("text/plain")
    elif filename.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


def formatans(a):
    #function to strip out spaces and lower cases
    a = a.lower().strip()
    return a


main()