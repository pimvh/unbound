# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

## Required variables

Review the variables as shown in defaults. Most have sensible defaults, you probably want to override some.

You probably want to pass interfaces, and additional access controls

```

---
unbound_interfaces:
  - "127.0.0.1"
  - "::1"
  - << another IP here >>
  - << another IP here >>

unbound_dns_port: "53"
unbound_do_ipv4: "yes"
unbound_do_ipv6: "yes"
unbound_forward_tls_upstream: "no"
unbound_prefer_ipv6: "yes"
unbound_do_udp: "yes"
unbound_do_tcp: "yes"
unbound_verbosity: "0"
unbound_log_queries: "no"
unbound_log_replies: "no"
unbound_log_tag_queryreply: "no"
unbound_log_local_actions: "no"
unbound_log_servfail: "no"
unbound_private_domains:
  - "home.lan"

# Only give access to recursion clients from LAN IPs
unbound_additional_access_controls:
  - cidr_range: 10.0.0.0/8
    action: allow
  - cidr_range: 127.0.0.0/8
    action: allow
  - cidr_range: 127.0.0.1/32
    action: allow
  - cidr_range: 172.16.0.0/12
    action: allow
  - cidr_range: 192.168.0.0/16
    action: allow
  - cidr_range: fc00::/7
    action: allow
  - cidr_range: ::1/128
    action: allow
  - cidr_range: << allow another range >>
    action: allow

unbound_local_zones: []
unbound_stub_zones: []
unbound_forward_zones: {}
```

The ansible playbook will validate whether the variables exist that you defined before running.

# Example playbook

```
hosts:
  - foo
roles:
  - pimvh.unbound

```

# TLDR - What will happen if I run this

- validate whether rules/some other variables are defined
- install unbound, when unbound_install
- push config
- point systemd-resolved of that system to unbound first
- verify whether Unbound resolved a domain

# Future Improvements

- Fetching roothints file
- Adding more variables to be set via Ansible

# License

The GPLv3 License (GPLv3)

Copyright (c) 2022 Author

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
