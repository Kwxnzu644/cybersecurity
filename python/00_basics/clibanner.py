import argparse

def banner(message, style):
    if style == "plain":
        print( " + " + " - " *  len(message ) + " + ")
        print(message)
        print( " + "  + " - " *  len(message) + " + ")
    elif style == "equals":
        print(" ="  * len(message))
        print(message)
        print(" = " * len(message))
    elif style == "box":
        print(" | " + " _ " * len(message) + " | ")
        print(message)
        print(" | " + " _ " * len(message) + " | ")
    else:
        print("Enter a valid style")


if __name__ == "__main__":
 parser=argparse.ArgumentParser(description="this is a style banner")

parser.add_argument("-m","--message", required=True , help="display the banner")

parser.add_argument("-s","--style", choices=["plain","box","equals"], default="plain" , help="diplay Styled Banner")

args=parser.parse_args()

banner(args.message,args.style)
