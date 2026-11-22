# honeytrace

a small fake ssh honeypot in python, built to see what attackers try. it listens on a port, shows an ssh-style banner and login prompt, logs every credential attempt, then drops the visitor into a fake shell and logs the commands they type.

## features

- fake ssh banner and login flow
- logs usernames and passwords from every attempt
- fake shell that records each command (it answers everything with `permission denied`)
- optional geoip lookup per source ip
- timestamped log written to `logs/honeytrace.log`
- python 3 standard library only

## run

```bash
python3 honeytrace.py            # listens on port 2222
nc localhost 2222                # connect from another terminal
```

## sample log

```
[2026-01-01 12:00:00] credentials from 203.0.113.7:51234 user=admin pass=admin123
[2026-01-01 12:00:04] cmd from 203.0.113.7:51234 -> ls
```

## notes

- each connecting ip is sent to `ipinfo.io` for the geoip lookup. remove `geo_lookup` if you do not want that.
- it binds to `0.0.0.0` and records plaintext passwords. run it on a network you own, ideally in a container or vm.

## license

mit. see license.
