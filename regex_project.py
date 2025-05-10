import re


def menu():
    print("\n🌟 Welcome to the Python REGEX Project 🌟")
    print("1️⃣ Extract Emails")
    print("2️⃣ Extract Phone Numbers")
    print("3️⃣ Extract Dates")
    print("4️⃣ Extract URLs")
    print("5️⃣ Validate Email")
    print("6️⃣ Validate Password")
    print("7️⃣ Replace Words")
    print("0️⃣ Exit")


def extract_emails(text: str) -> str:
    """Return email addresses if any are found."""
    email_regex = r"\b[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
    matches = re.findall(email_regex, text)
    if matches:
        results = ""
        for match in matches:
            results += "".join(match) + '\n'
        return results
    return "No results."


def extract_phone_numbers(text: str) -> str:
    """Return phone numbers if any are found. The phone number format (regex) is based in the United States."""
    phone_number_regex = r"\+1\s\d{3}-\d{3}-\d{4}"
    matches = re.findall(phone_number_regex, text)
    return ", ".join(matches) if matches else ("No results. The program only accepts "
                                               "phone numbers in the US format +1 111-111-1111.")


def extract_dates(text: str) -> str:
    """Return dates if any are found. The date formats are DD/MM/YYYY, MM-DD-YYYY and DD MMM YYYY."""
    date_format1 = r"\d{2}\/\d{2}\/\d{4}"  # DD/MM/YYYY (e.g. 25/05/2025)
    date_format2 = r"\b\d{2}-\d{2}-\d{4}\b"  # MM-DD-YYYY (e.g. 05-25-2025)
    date_format3 = r"\d{2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}"  # DD MMM YYYY (e.g. 25 May 2025)

    matches1 = re.findall(date_format1, text)
    matches2 = re.findall(date_format2, text)
    matches3 = re.findall(date_format3, text)

    results = ""
    if matches1:
        results += ' '.join(matches1) + ' '
    if matches2:
        results += ' '.join(matches2) + ' '
    if matches3:
        results += ', '.join(matches3)

    if results:
        return results
    return "No results."


def extract_urls(text: str) -> str:
    """Return URLs if any are found. The subdomain will always be 'www'."""
    url_regex = r"(https:\/\/)?(www\.)?([a-zA-Z0-9\-]+)((\.[a-z]+)+)((\/[a-zA-Z]+)+)?"
    matches = re.findall(url_regex, text)

    if matches:
        result = ""
        for match in matches:
            url = f"{match[0]}{match[1]}{match[2]}{match[3]}{match[5]}"
            result += url + "\n"
        return result
    return "No results."


def validate_email(email: str) -> str:
    """Check if an email is valid."""
    email_regex = r"\b[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
    match = re.match(email_regex, email)
    return "This email is valid." if match else "This email is invalid."


def validate_password(password: str) -> str:
    """Check if a password is valid."""
    password_regex = r"^(?=(.*[a-z]))(?=(.*[A-Z]))(?=(.*[0-9]))(?=(.*[@$!%*?&]))[A-Za-z\d@$!%*?&]{8,}$"
    match = re.match(password_regex, password)
    return "This password is strong." if match else "This password is weak."


def replace_word(text: str, old_word: str, new_word: str) -> str:
    """Replace all occurrences of old_word with new_word, case-sensitive."""
    pattern = fr"{old_word}"
    replacement = fr"{new_word}"
    if old_word in text:
        return re.sub(pattern, replacement, text)
    return "The word you were trying to replace is not in the text."


def main():
    """The main program for the Python REGEX Project."""

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter a text: ")
            print(extract_emails(text))

        elif choice == '2':
            text = input("Enter a text: ")
            print(extract_phone_numbers(text))

        elif choice == '3':
            text = input("Enter a text: ")
            print(extract_dates(text))

        elif choice == '4':
            text = input("Enter a text: ")
            print(extract_urls(text))

        elif choice == '5':
            email = input("Enter an email: ")
            print(validate_email(email))

        elif choice == '6':
            password = input("Enter a password: ")
            print(validate_password(password))

        elif choice == '7':
            text = input("Enter a text: ")
            old_word = input("Enter a word from the text: ")
            new_word = input("Enter a replacement word: ")
            print(replace_word(text, old_word, new_word))

        elif choice == '0':
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
