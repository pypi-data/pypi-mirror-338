import os
import json
from bugscanx.utils.common import get_input, get_confirm
from .scanners.direct import DirectScanner
from .scanners.proxy_check import ProxyScanner
from .scanners.proxy_request import Proxy2Scanner
from .scanners.ssl import SSLScanner
from .scanners.ping import PingScanner

def read_hosts(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

def get_common_inputs(filename):
    output = get_input("Enter output filename", default=f"result_{os.path.basename(filename)}", validate_input=False)
    threads = get_input("Enter threads", "number", default="50")
    return output, threads

def get_input_direct(no302=False):
    filename = get_input("Enter filename", "file")
    port_list = get_input("Enter ports", "number", default="80").split(',')
    output, threads = get_common_inputs(filename)
    method_list = get_input("Select HTTP method", "choice", multiselect=True, 
                           choices=["GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "TRACE", "PATCH"])
    
    scanner = DirectScanner()
    scanner.method_list = method_list
    scanner.host_list = read_hosts(filename)
    scanner.port_list = port_list
    scanner.no302 = no302
    
    return scanner, output, threads

def get_input_proxy():
    filename = get_input("Enter proxies filename", "file")
    target_url = get_input("Enter target url", default="in1.wstunnel.site")
    method = get_input("Enter HTTP method", default="GET")
    path = get_input("Enter path", default="/")
    protocol = get_input("Enter protocol", default="HTTP/1.1")
    default_payload = (
        "[method] [path] [protocol][crlf]"
        "Host: [host][crlf]"
        "Connection: Upgrade[crlf]"
        "Upgrade: websocket[crlf][crlf]"
    )
    payload = get_input("Enter payload", default=default_payload)
    port_list = get_input("Enter ports", "number", default="80").split(',')
    output, threads = get_common_inputs(filename)
    bug = get_input("Enter bug (optional)", default="", validate_input=False)
    
    scanner = ProxyScanner()
    scanner.host_list = read_hosts(filename)
    scanner.target = target_url
    scanner.method = method
    scanner.path = path
    scanner.protocol = protocol
    scanner.bug = bug
    scanner.payload = payload
    scanner.port_list = port_list
    
    return scanner, output, threads

def get_input_proxy2():
    filename = get_input("Enter filename", "file")
    port_list = get_input("Enter ports", "number", default="80").split(',')
    output, threads = get_common_inputs(filename)
    method_list = get_input("Select HTTP method", "choice", multiselect=True, 
                           choices=["GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "TRACE", "PATCH"])
    
    proxy = get_input("Enter proxy (proxy:port)")
    
    use_auth = get_confirm(" Use proxy authentication?")
    proxy_username = None
    proxy_password = None
    
    if use_auth:
        proxy_username = get_input("Enter proxy username")
        proxy_password = get_input("Enter proxy password")
    
    scanner = Proxy2Scanner()
    scanner.set_proxy(proxy, proxy_username, proxy_password)
    scanner.method_list = method_list
    scanner.host_list = read_hosts(filename)
    scanner.port_list = port_list
    
    return scanner, output, threads

def get_input_ssl():
    filename = get_input("Enter filename", "file")
    output, threads = get_common_inputs(filename)
    
    scanner = SSLScanner()
    scanner.host_list = read_hosts(filename)
    
    return scanner, output, threads

def get_input_ping():
    filename = get_input("Enter filename", "file")
    port_list = get_input("Enter ports", "number", default="443").split(',')
    output, threads = get_common_inputs(filename)
    
    scanner = PingScanner()
    scanner.host_list = read_hosts(filename)
    scanner.port_list = port_list
    
    return scanner, output, threads

def get_user_input():
    mode = get_input("Select mode", "choice", 
                    choices=["direct", "direct-no302", "proxy-check", "proxy-request", "ping", "ssl"])
    
    input_handlers = {
        'direct': lambda: get_input_direct(no302=False),
        'direct-no302': lambda: get_input_direct(no302=True),
        'proxy-check': get_input_proxy,
        'proxy-request': get_input_proxy2,
        'ping': get_input_ping,
        'ssl': get_input_ssl
    }
    
    scanner, output, threads = input_handlers[mode]()
    return scanner, output, threads, mode

def main():
    scanner, output, threads, mode = get_user_input()
    scanner.threads = int(threads)
    scanner.start()

    if output:
        with open(output, 'a+') as file:
            if mode == 'proxy-check':
                json.dump(scanner.success_list(), file, indent=2)
            else:
                file.write('\n'.join([str(x) for x in scanner.success_list()]) + '\n')
