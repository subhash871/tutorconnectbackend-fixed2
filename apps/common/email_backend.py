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