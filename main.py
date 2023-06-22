from PyIpify.synchronous import find_ipv4, find_ipv6


# noinspection PyCallingNonCallable
def main():
    ipv4 = find_ipv4()
    ipv6 = find_ipv6()
    print(f'IPv4: {ipv4}')
    print(f'IPv6: {ipv6}')


if __name__ == '__main__':
    main()
