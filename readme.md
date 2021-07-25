# A python DDNS Script for Cloudflare

Update `A` and `AAAA` record for domains in Cloudflare.

## Dependences

- requests

## How to use

### Install Dependences
```
pip install requests 
```

### Configuration

Modify `config.py` and input your infomation.

- cf_email: Account email in Cloudflare
- cf_key: Cloudflare API key
- zone_name: Zone Name in Cloudflare
- domain: domain for DDNS
- ipv6: Set to `True` to update AAAA record

### Run

```
python ddns.py
```

You can use `crontab` or `systemd` to execute the `python ddns.py` periodly.

