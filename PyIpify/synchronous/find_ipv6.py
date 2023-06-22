import requests


def find_ipv6():
    """Return the public IPv6 address of the system.
    This function is synchronous.
    
    Returns:
        str: The IPv6 address of the client.
        
        Example:
            >>> from PyIpify.synchronous import find_ipv6
            >>> find_ipv6()
    """
    return requests.get('https://api6.ipify.org?format=json').json()['ip']
