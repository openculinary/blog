import argparse
from collections import defaultdict
import email
from email import policy
import string

from dateutil.parser import parse as parse_datetime
import html5lib
from textunwrap.textunwrap import unwrap
from urlextract import URLExtract


parser = argparse.ArgumentParser("Convert an EML file into Markdown format")
parser.add_argument("filename", type=str, help="EML input filename")
args = parser.parse_args()


def extract_hyperlink_phrases(html):
    parse_tree = html5lib.parse(message_html)
    hyperlink_phrases = defaultdict(set)
    for anchor in parse_tree.iter("{http://www.w3.org/1999/xhtml}a"):
        destination = anchor.attrib["href"]
        hyperlink_phrases[destination] = anchor.text
    return hyperlink_phrases


def extract_hyperlinks(text):
    extractor = URLExtract()
    return extractor.find_urls(text)


if __name__ == "__main__":
    with open(args.filename) as f:
        message = email.message_from_file(f, policy=policy.default)
        message_plain = message.get_body("plain").get_content()
        message_html = message.get_body("html").get_content()

        hyperlink_phrases = extract_hyperlink_phrases(message_html)

        text = unwrap(message_plain)
        output = ""
        for line in text.split("\n"):

            # Note: image markers require manual edits to add labels
            line = line.replace("[image: ", "[placeholder](")
            line = line.replace("]", ' "placeholder")')

            # Replace GMail text/plain-formatted hyperlinks with Markdown links
            for hyperlink in extract_hyperlinks(line):
                phrase = hyperlink_phrases[hyperlink]
                pattern = f"{phrase} <{hyperlink}>"
                substitution = f"[{phrase}]({hyperlink})"
                line = line.replace(pattern, substitution)

            # Attempt to naively match text emphasis (bold and italic)
            tokens = []
            delimiter = "**"
            for word in line.split():
                if word.startswith("*") and word.endswith("*"):
                    is_bold = word[1] in string.ascii_uppercase
                    delimiter = "**" if is_bold else "_"
                    tokens.append(f"{delimiter}{word[1:-1]}{delimiter}")
                    continue

                if word.startswith("*"):
                    is_bold = word[1] in string.ascii_uppercase
                    delimiter = "**" if is_bold else "_"
                    tokens.append(f"{delimiter}{word[1:]}")
                    continue

                if word.endswith("*"):
                    tokens.append(f"{word[:-1]}{delimiter}")
                    continue

                tokens.append(word)

            # Emit the line
            output += " ".join(tokens)
            output += "\n"

        # Write to an appropriately-timestamped blog post filename
        sent = parse_datetime(message["Date"])
        post_filename = f"../content/posts/fortnightly-update-{sent:%Y-%m-%d}.md"
        with open(post_filename, "w") as post:
            post.write(output)

        # Write dependent attachments to the static images directory
        # NB: Non-image attachments will require manual adjustment
        for attachment in message.iter_attachments():
            with open(f"../static/images/{attachment.get_filename()}", "wb") as f:
                f.write(attachment.get_content())
