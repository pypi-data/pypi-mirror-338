<!--
SPDX-FileCopyrightText: 2025 Anthony Zimmermann

SPDX-License-Identifier: GPL-3.0-only
-->

# KMC - Keyboard Mouse Connect

Forward keyboard and mouse input to another machine via a software communication protocol like ethernet.

Find installation examples below for using KMC. The examples include the installation of KMC itself plus systemd service configurations to enable a seamless integration into the system start. KMC itself does not deal with a secure connection at all. Other applications like ssh tunnels can be used to create encrypted connections.

## Running KMC client

With a client configuration file `kmc.conf`, kmc client could be executed like this:

```bash
kmc -c kmc.conf
```

### Example installation via pipx

Using pipx, we can install kmc globally via the following command:

```bash
sudo PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx install kmc
```

With kmc installed globally, a systemd service could be installed into '~/.config/systemd/user/kmc.service':

```ini
# Filename: kmc.service
[Unit]
Description=KMC client
After=network.target

[Service]
Environment=DISPLAY=:0
ExecStart=/usr/local/bin/kmc -c ~/.config/kmc.conf
Restart=always

[Install]
WantedBy=default.target
```

The systemd service could be enabled to load automatically on boot:

```bash
systemctl --user enable kmc
```

### Example client configuration

```
# Filename: kmc.conf
[display.tcp.kmc-server-host]
host = kmc-server-host-hostname
port = 12345
keymap = <shift>+<ctrl>+<up>
```

## Running KMC server

With a server configuration file `kmc-server.conf`, kmc server can be executed like this:

```bash
kmc-server -c kmc-server.conf
```

### Example installation via pipx

Using pipx, we can install kmc globally via the following command.

```bash
sudo PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx install kmc
```

With kmc installed globally, a systemd service could be installed.

```ini
# Filename: kmc-server.service
[Unit]
Description=KMC server
After=network.target

[Service]
Environment=DISPLAY=:0
ExecStart=/usr/local/bin/kmc-server -c /etc/kmc-server.conf
Restart=always

[Install]
WantedBy=multi-user.target
```

The systemd service could be enabled to load automatically on boot:

```bash
systemctl enable kmc-server
```

### Example server configuration

```
# Filename: kmc-server.conf
[display.tcp.kmc-server-host]
host = 0.0.0.0
port = 12345
```

---

**KMC Version 1.0.1<!-- VERSION -->**

---
