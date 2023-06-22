from PyIpify.syncronous import find_ipv4, find_ipv6


def main():
    ipv4 = find_ipv4()
    ipv6 = find_ipv6()
    print(f'IPv4: {ipv4}')
    print(f'IPv6: {ipv6}')


if __name__ == '__main__':
    main()
