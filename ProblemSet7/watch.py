import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    src = re.search(r"(?:<iframe)[^>]*(?:src=\")https?://(?:www\.)?(?:youtube)\.com/embed/([a-z0-9_-]+)", s, re.IGNORECASE)
    if src:
        video_id = src.group(1)
        # print(video_id)
        return (f"https://youtu.be/{video_id}")
    return None

if __name__ == "__main__":
    main()