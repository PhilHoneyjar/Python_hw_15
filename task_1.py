import argparse
import logging
from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        obj = super(MyStr, cls).__new__(cls, value)
        obj.value = value
        obj.author = author
        obj.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return obj

    def __str__(self):
        return f"Event: {self.value}\nAuthor: {self.author}\nTime: {self.time}"

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"


def main():
    parser = argparse.ArgumentParser(description='Event Journal')
    parser.add_argument('--value', type=str, help='Event description')
    parser.add_argument('--author', type=str, help='Author name')
    args = parser.parse_args()

    if not args.value or not args.author:
        logging.basicConfig(filename='event.log', level=logging.ERROR)
        logging.error("Missing required arguments. Both --value and --author are mandatory.")
    else:
        event = MyStr(args.value, args.author)
        logging.basicConfig(filename='event.log', level=logging.INFO)
        logging.info(f"New event created: {event}")


if __name__ == "__main__":
    main()
