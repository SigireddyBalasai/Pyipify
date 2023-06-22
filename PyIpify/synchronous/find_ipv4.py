import requests


def find_ipv4():
    """Return the public IPv4 address of the system.
    This function is synchronous.
    
    Returns:
        str: The IPv4 address of the client.
        
        Example:
            >>> from PyIpify.synchronous import find_ipv4
            >>> find_ipv4()
            
    """
    return requests.get('https://api.ipify.org?format=json').json()['ip']
