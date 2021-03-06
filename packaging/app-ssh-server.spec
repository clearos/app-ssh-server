
Name: app-ssh-server
Epoch: 1
Version: 2.4.0
Release: 1%{dist}
Summary: SSH Server
License: GPLv3
Group: ClearOS/Apps
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base
Requires: app-network

%description
The SSH Server app provides the tools to manage secure shell policies for your system.

%package core
Summary: SSH Server - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-network-core >= 1:2.4.2
Requires: openssh-server >= 5.3p1

%description core
The SSH Server app provides the tools to manage secure shell policies for your system.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/ssh_server
cp -r * %{buildroot}/usr/clearos/apps/ssh_server/

install -d -m 0755 %{buildroot}/var/clearos/ssh_server
install -d -m 0755 %{buildroot}/var/clearos/ssh_server/backup
install -D -m 0644 packaging/attack-detector-sshd-ddos.php %{buildroot}/var/clearos/attack_detector/filters/sshd-ddos.php
install -D -m 0644 packaging/attack-detector-sshd.php %{buildroot}/var/clearos/attack_detector/filters/sshd.php
install -D -m 0644 packaging/clearos-sshd-ddos.conf %{buildroot}/etc/fail2ban/jail.d/clearos-sshd-ddos.conf
install -D -m 0644 packaging/clearos-sshd.conf %{buildroot}/etc/fail2ban/jail.d/clearos-sshd.conf
install -D -m 0644 packaging/sshd.php %{buildroot}/var/clearos/base/daemon/sshd.php

%post
logger -p local6.notice -t installer 'app-ssh-server - installing'

%post core
logger -p local6.notice -t installer 'app-ssh-server-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/ssh_server/deploy/install ] && /usr/clearos/apps/ssh_server/deploy/install
fi

[ -x /usr/clearos/apps/ssh_server/deploy/upgrade ] && /usr/clearos/apps/ssh_server/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-ssh-server - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-ssh-server-core - uninstalling'
    [ -x /usr/clearos/apps/ssh_server/deploy/uninstall ] && /usr/clearos/apps/ssh_server/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/ssh_server/controllers
/usr/clearos/apps/ssh_server/htdocs
/usr/clearos/apps/ssh_server/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/ssh_server/packaging
%exclude /usr/clearos/apps/ssh_server/unify.json
%dir /usr/clearos/apps/ssh_server
%dir /var/clearos/ssh_server
%dir /var/clearos/ssh_server/backup
/usr/clearos/apps/ssh_server/deploy
/usr/clearos/apps/ssh_server/language
/usr/clearos/apps/ssh_server/libraries
/var/clearos/attack_detector/filters/sshd-ddos.php
/var/clearos/attack_detector/filters/sshd.php
%config(noreplace) /etc/fail2ban/jail.d/clearos-sshd-ddos.conf
%config(noreplace) /etc/fail2ban/jail.d/clearos-sshd.conf
/var/clearos/base/daemon/sshd.php
