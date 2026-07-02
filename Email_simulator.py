import datetime

class Email:
    """
    Represents an email with sender, receiver, subject, body,
    timestamp, and read status.
    """

    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self):
        """Mark the email as read."""
        self.read = True

    def display_full_email(self):
        """Display the complete email details."""
        self.mark_as_read()

        print("\n--- Email ---")
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f"Body: {self.body}")
        print("--------------\n")

    def __str__(self):
        """Return a short summary of the email."""
        status = "Read" if self.read else "Unread"

        return (
            f"[{status}] "
            f"From: {self.sender.name} | "
            f"Subject: {self.subject} | "
            f"Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        )


class User:
    """
    Represents a user who can send, receive,
    read, and delete emails.
    """

    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        """Send an email to another user."""
        email = Email(
            sender=self,
            receiver=receiver,
            subject=subject,
            body=body,
        )

        receiver.inbox.receive_email(email)

        print(f"Email sent from {self.name} to {receiver.name}!\n")

    def check_inbox(self):
        """Display all emails in the inbox."""
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        """Read an email by its index."""
        self.inbox.read_email(index)

    def delete_email(self, index):
        """Delete an email by its index."""
        self.inbox.delete_email(index)


class Inbox:
    """
    Stores and manages all received emails.
    """

    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        """Receive a new email."""
        self.emails.append(email)

    def list_emails(self):
        """Display all emails in the inbox."""

        if not self.emails:
            print("Your inbox is empty.\n")
            return

        print("\nYour Emails:")

        for index, email in enumerate(self.emails, start=1):
            print(f"{index}. {email}")

    def read_email(self, index):
        """Display a selected email."""

        if not self.emails:
            print("Inbox is empty.\n")
            return

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
            return

        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        """Delete a selected email."""

        if not self.emails:
            print("Inbox is empty.\n")
            return

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
            return

        del self.emails[actual_index]

        print("Email deleted.\n")


def main():
    """Program entry point."""

    # Create users
    saurabh = User("saurabh")
    ganguli = User("ganguli")

    # Send emails
    saurabh.send_email(ganguli,"Hello","Hi ganguli, just saying hello!")

    ganguli.send_email(saurabh,"Re: Hello","Hi saurabh, hope you are fine.")

    # Check inbox
    ganguli.check_inbox()

    # Read first email
    ganguli.read_email(1)

    # Delete first email
    ganguli.delete_email(1)

    # Check inbox again
    ganguli.check_inbox()


if __name__ == "__main__":
    main()
