#! /usr/bin/env python3
#
# Date:    2024/12/12
# Author:  Andy Pérez
#
# Module to send emails with.

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import split as pathsplit

class Mail:
	def __init__(
			self,
			host: str, port: int = 587,
			sender: str|None = None, recipients: str|list|tuple|None = None,
			subject: str|None = None,
			body: str|None = None,
			attachments: str|dict|None = None,):
		"""
		Starts an SMTP server.

		Args:
			host: SMTP host server.
			port: SMPT port to use (default is 587).
		"""
		self.attachments: list = []
		self.bodytext: str = ""
		self.server: SMTP = SMTP(host, port)
		self.mail: MIMEMultipart = MIMEMultipart()
		if sender: self.sender = sender
		if recipients: self.recipients = recipients
		if subject: self.subject = subject
		if body: self.body = body
		if attachments: self.attach(attachments)
		return

	def __str__(self) -> str:
		recipients = '\033[0m, \033[4m'.join(self.recipients or [])
		body: str = self.body or "(no body)"
		subject: str = self.subject or "(no subject)"
		attachments: str = ' '.join([f'\033[4;7;34m{a}\033[0m' for a in self.attachments])
		rstr = f"""	\033[1m{subject}\033[0m
	From: \033[4m{self.sender}\033[0m
	To:   \033[4m{recipients}\033[0m

	{body}

	{attachments}"""
		return rstr
	@property
	def subject(self) -> str:
		if "Subject" not in self.mail: return ''
		return self.mail["Subject"]
	@subject.setter
	def subject(self, item: str) -> None:
		try:
			self.mail.replace_header("Subject", item)
		except KeyError:
			self.mail['Subject'] = item

	@property
	def body(self) -> str: return self.bodytext
	@body.setter
	def body(self, item: str) -> None:
		if self.bodytext:
			# Unattach
			payload = self.mail.get_payload()
			if isinstance(payload, list):
				for part in payload:
					if not isinstance(part, MIMEText): continue
					payload.remove(part)
					break
		self.mail.attach(MIMEText(item))
		self.bodytext = item

	@property
	def sender(self) -> str|None:
		if "From" not in self.mail: return None
		return self.mail["From"]
	@sender.setter
	def sender(self, item: str) -> None: self.mail["From"] = item

	@property
	def recipients(self) -> str|tuple[str, ...]|None:
		if "To" not in self.mail: return None
		return tuple(r.strip() for r in self.mail['To'].split(","))
	@recipients.setter
	def recipients(self, item: str|list[str]|tuple[str, ...]) -> None:
		if isinstance(item, str):
			self.mail['To'] = item
			return
		self.mail['To'] = ', '.join(item)

	def attach_single(self, file: str|bytes, filename: str|None = None) -> None:
		"""
		Attaches a `file` with `filename`.

		Args:
			file: Bytes or path of the file.
			filename: Filename given inside the mail.
			mail: Mail to attach file to.
		
		Raises:
			TypeError: Expected path (str) or file (bytes) but got `file` (`type(file)`).
		"""
		if not isinstance(file, str|bytes):
			raise TypeError(f'Expected path (str) or file (bytes) but got "{file}" ({type(file)}).')
		if isinstance(file, str):
			with open(file, "rb") as f: fbytes = f.read()
		else:
			fbytes = file
		self.attachments.append(filename)
		self.mail.attach(MIMEApplication(
			fbytes,
			Name = filename
		))
		return

	def attach(self, files: str|bytes|dict[str, str|bytes], filename: str|None = None) -> None:
		if isinstance(files, bytes) and not filename:
			raise TypeError('`filename` is required when a `bytes` object is given.')
		if isinstance(files, str) and not filename:
			filename = pathsplit(files)[1]
		if not isinstance(files, dict):
			self.attach_single(files, filename)
			return
		for name, file in files.items():
			if not (isinstance(name, str) and isinstance(file, str|bytes)):
				raise TypeError("Items in the dictionary must be in the form of `{str: str | bytes}`.")
			self.attach_single(file, name)
		return

	def send(self, password) -> bool:
		try:
			self.server.starttls()
			if self.sender is None:
				raise ValueError("Sender is not set.")
			if self.recipients is None:
				raise ValueError("There is no recipient set.")
			self.server.login(self.sender, password)
			self.server.sendmail(self.sender, self.recipients, self.mail.as_string())
			self.server.quit()
			return True
		except Exception as e:
			print(f"Failed to send email: {e}")
			return False

	def save(self, path: str) -> None:
		with open(path, "w") as f:
			f.write(self.mail.as_string())
		return

class Gmail(Mail):
	def __init__(self,
			sender: str|None = None, recipients: str|list|tuple|None = None,
			subject: str|None = None,
			body: str|None = None,
			attachments: str|dict|None = None,):
		super().__init__('smtp.gmail.com', 587, sender, recipients, subject, body, attachments)
		return

def main() -> None: return

if __name__ == '__main__': main()
