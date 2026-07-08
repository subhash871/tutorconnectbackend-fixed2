"""
Custom SMTP email backend that forces IPv4 connections.

Render's network doesn't reliably route outbound IPv6 traffic, which
causes `OSError(101, 'Network is unreachable')` when Python's smtplib
resolves an SMTP host (e.g. smtp.gmail.com) to an IPv6 address first.
Forcing IPv4 avoids this entirely.
"""
import smtplib
import socket

from django.core.mail.backends.smtp import EmailBackend as DjangoSMTPBackend


class IPv4SMTP(smtplib.SMTP):
    """smtplib.SMTP subclass that only resolves/connects over IPv4."""

    def _get_socket(self, host, port, timeout):
        if timeout is not None and not timeout:
            raise ValueError('Non-blocking socket (timeout=0) is not supported')
        addr_info = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
        family, socktype, proto, _, sockaddr = addr_info[0]
        sock = socket.socket(family, socktype, proto)
        if timeout is not None:
            sock.settimeout(timeout)
        sock.connect(sockaddr)
        return sock


class IPv4EmailBackend(DjangoSMTPBackend):
    """Django SMTP email backend that forces the underlying connection to IPv4."""

    def open(self):
        if self.connection:
            return False
        connection_class = IPv4SMTP
        try:
            self.connection = connection_class(
                self.host, self.port, timeout=self.timeout
            )
            if not self.use_ssl and self.use_tls:
                self.connection.starttls()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except OSError:
            if not self.fail_silently:
                raise
            return False


class ResendEmailBackend:
    """
    Minimal Django email backend using the Resend HTTP API
    (https://resend.com). Render (and many PaaS providers) block
    outbound SMTP ports entirely on free tiers, so SMTP-based sending
    cannot work there. Resend sends over plain HTTPS (port 443),
    which is never blocked.

    Requires RESEND_API_KEY to be set.
    """

    def __init__(self, fail_silently=False, **kwargs):
        self.fail_silently = fail_silently

    def send_messages(self, email_messages):
        import requests
        from django.conf import settings

        api_key = getattr(settings, 'RESEND_API_KEY', '')
        if not api_key:
            if self.fail_silently:
                return 0
            raise ValueError('RESEND_API_KEY is not set.')

        sent_count = 0
        for message in email_messages:
            try:
                response = requests.post(
                    'https://api.resend.com/emails',
                    headers={'Authorization': f'Bearer {api_key}'},
                    json={
                        'from': message.from_email,
                        'to': message.to,
                        'subject': message.subject,
                        'text': message.body,
                    },
                    timeout=10,
                )
                response.raise_for_status()
                sent_count += 1
            except Exception:
                if not self.fail_silently:
                    raise
        return sent_count