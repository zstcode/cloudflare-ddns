# A python DDNS Script for Cloudflare

Update `A` and `AAAA` record for domains in Cloudflare.

## Dependences

- requests

## How to use

### Install Dependences
```
pip install requests 
```

### Set up API Token

Set up an API token in Cloudflare for editing DNS records of the domain.

### Configuration

Modify `config.py` and input your infomation.

- cf_api_token: Cloudflare API Token for DNS editing
- zone_name: Zone Name in Cloudflare
- domain: domain for DDNS
- ipv6: Set to `True` to update AAAA record

### Run

```
python ddns.py
```

You can use `crontab` or `systemd` to execute the `python ddns.py` periodly.

