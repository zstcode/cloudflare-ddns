import requests
import socket
import os
from config import cf_email, cf_key, zone_name, domain, ipv6


def get_ip(ip_type):
    ip_test = {"A": "1.1.1.1", "AAAA": "2606:4700:4700::1111"}
    ip = None
    try:
        s = socket.socket(
            socket.AF_INET if ip_type == "A" else socket.AF_INET6, socket.SOCK_DGRAM
        )
        s.connect((ip_test.get(ip_type), 53))
        ip = s.getsockname()[0]
    finally:
        s.close()
        return ip


def set_ip(ip, ip_type):
    global zone_id, auth_headers, domain
    url_get_dns_record = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type={ip_type}&name={domain}"
    json_data = {"type": ip_type, "name": f"{domain}", "content": ip}
    try:
        dns_record = requests.get(url_get_dns_record, headers=auth_headers).json()[
            "result"
        ][0]
        dns_record_ip = dns_record.get("content", "")
        dns_record_id = dns_record.get("id", "")
        if dns_record_ip != ip:
            url_put_record = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record_id}"
            requests.put(url_put_record, headers=auth_headers, json=json_data)
    except IndexError:
        url_post_record = (
            f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
        )
        requests.post(url_post_record, headers=auth_headers, json=json_data)


if __name__ == "__main__":
    auth_headers = {
        "X-Auth-Email": cf_email,
        "X-Auth-Key": cf_key,
        "Content-Type": "application/json",
    }
    url_get_zone_id = f"https://api.cloudflare.com/client/v4/zones?name={zone_name}"

    try:
        zone_id = requests.get(url_get_zone_id, headers=auth_headers).json()["result"][
            0
        ]["id"]
    except IndexError:
        exit("No zones found")
    except TypeError:
        exit("Auth error")
    set_ip(get_ip("A"), "A")
    if ipv6:
        set_ip(get_ip("AAAA"), "AAAA")
