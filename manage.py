from scripts.alters import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("option", help="select the option")
    parser.add_argument("suboption", nargs="?", help="suboption of the option")
    parser.add_argument("-i", "--index", type=int, help="index")
    parser.add_argument("-f", "--file", help="file directory")
    parser.add_argument("-f2", "--file2")
    parser.add_argument("-l", "--link", help="hyperlink")
    parser.add_argument("-t", "--text", help="text")
    parser.add_argument("-col", "--column", type=int)
    parser.add_argument("-row", "--row", type=int)
    args = parser.parse_args()
    
    if args.option == "change":
        if args.suboption == "square-link":
            change_square_link(args.index, args.link)
        elif args.suboption == "square-text":
            change_square_text(args.index, args.text)
        elif args.suboption == "square-description":
            change_square_description(args.index, args.text)
        # elif args.suboption == "gallery-picture":
        #     change_gallery_picture(args.row, args.column, args.file, args.file2)
        else:
            print("Warning: no action is taken.")
    elif args.option == "create":
        if args.suboption == "article":
            create_page(args.file, args.link)
        else:
            print("Warning: no action is taken.")
    elif args.option =="insert":
        if args.suboption == "article":
            insert_article(args.text, args.link)
        else:
            print("Warning: no action is taken.")
    elif args.option == "remove":
        if args.suboption == "article":
            remove_article(args.index)
    else:
        print("Warning: no action is taken.")
