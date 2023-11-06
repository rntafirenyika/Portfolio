"""
Prompts the user for a greeting. If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20.
Otherwise, output $100.
Any leading whitespace in the user's greeting is ignored and the user's greeting is treated case-insensitively.
"""
def main():
#Prompt the user for a greeting
    reward = value(input("Greeting: ").strip())
    print(f"${reward}")

def value(greeting):
    #Diplays reward if greeting does not start with hello
        greeting = greeting.lower()
        if greeting.startswith("hello"):
            return 0
        elif greeting.startswith("h"):
            return 20
        else:
            return 100

if __name__ == "__main__":
    main()