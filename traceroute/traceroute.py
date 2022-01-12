import socket
import struct

__all__ = ["Traceroute"]


class Traceroute:
    def __init__(
        self,
        dest_name: str,
        dest_ip: str,
        port: int,
        first_hop: int = 1,
        max_hops: int = 64,
    ):
        self._dest = dest_name
        self._dest_ip = dest_ip
        self._max_hops = max_hops
        self._ttl = first_hop
        self._port = port

    def print_trace(self):
        print(
            f"traceroute to {self._dest} ({self._dest_ip}), {self._max_hops} hops max"
        )
        while self._ttl <= self._max_hops:
            receiver = self._create_receiver()
            sender = self._create_sender(self._ttl)
            sender.sendto(bytes(), (self._dest, self._port))
            try:
                _, addr = receiver.recvfrom(1024)
                addr = addr[0]
                print(f"{self._ttl}   {addr}")

                if addr == self._dest_ip:
                    break
            except socket.error:
                print(f"{self._ttl}   *")
            finally:
                receiver.close()
                sender.close()

            self._ttl += 1

    def _create_receiver(self):
        receiver = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_ICMP
        )
        timeout = struct.pack("ll", 5, 0)
        receiver.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

        try:
            receiver.bind(("", self._port))
        except socket.error as e:
            raise IOError(f"Failed to bind receiver socket: {e}")

        return receiver

    def _create_sender(self, ttl: int):
        sender = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP
        )
        sender.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)

        return sender
