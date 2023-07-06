import re

def main():
    url = parse(input("URL: ").strip())
    print(f"Entered: {url}")


def parse(s):
    if matches := re.search(r".+\"(?:(?:(?:http)s?)?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)(\".+)$", s, re.IGNORECASE):
        c_url = matches.group(1)
        return(f"https://youtu.be/{c_url}")


if __name__ == "__main__":
    main()