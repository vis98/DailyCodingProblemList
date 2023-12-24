
import imaplib
import email
import os

# Email server configuration
mail_server = "imap.gmail.com"  # Replace with your server
username = ""
password = ""
# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(mail_server)
mail.login(username, password)

# Select the inbox
mail.select("inbox")
target_subject = "Daily Coding Problem: Problem"  # Replace with the actual subject

# Search for emails with the specified subject
status, data = mail.search(None, f'(SUBJECT "{target_subject}")')
print("start====")

# Iterate through emails
for num in data[0].split():
    print("==")  # Optional for visual separation
    try:
        status, data = mail.fetch(num, "(RFC822)")
        message = email.message_from_bytes(data[0][1])

        # Check for important emails (modify this condition)
        if message['Subject']:  # Example condition
            # Extract email body
            body = ""
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break

            # Save email body to file
            filename = f"email_{num}.txt"  # Unique filename using email ID
            with open(filename, "w") as f:  # Use "w" mode for writing
                f.write(body)  # Use f.write(), not f.append()

    except Exception as e:
        print(f"Error processing email {num}: {e}")

print("end====")
# Close the connection
mail.close()
mail.logout()