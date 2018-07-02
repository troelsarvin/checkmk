DISTRO_CODE     = artful
BUILD_PACKAGES  =
BUILD_PACKAGES += build-essential
BUILD_PACKAGES += devscripts
BUILD_PACKAGES += dpatch
BUILD_PACKAGES += dnsutils
BUILD_PACKAGES += fping
BUILD_PACKAGES += smbclient # otherwise missing path in util.pm
BUILD_PACKAGES += rpcbind # otherwise missing path in util.pm
BUILD_PACKAGES += git-buildpackage
BUILD_PACKAGES += libboost-all-dev
BUILD_PACKAGES += libcloog-ppl1
BUILD_PACKAGES += libcurl4-openssl-dev # needed by perl modules / thruk
BUILD_PACKAGES += libevent-dev
BUILD_PACKAGES += libgd-dev
BUILD_PACKAGES += libglib2.0-dev
BUILD_PACKAGES += libgnutls28-dev
BUILD_PACKAGES += libldap2-dev
BUILD_PACKAGES += libltdl-dev
BUILD_PACKAGES += libmcrypt-dev
BUILD_PACKAGES += libmysqlclient-dev
BUILD_PACKAGES += libpq-dev
BUILD_PACKAGES += libpango1.0-dev
BUILD_PACKAGES += libperl-dev
BUILD_PACKAGES += libreadline-dev
BUILD_PACKAGES += libssl-dev
BUILD_PACKAGES += libxml2-dev
BUILD_PACKAGES += libsqlite3-dev # needed by Python (for sqlite3 module)
BUILD_PACKAGES   += tk-dev # needed by Python (for Tkinter module)
BUILD_PACKAGES += patch
BUILD_PACKAGES += rsync
BUILD_PACKAGES += uuid-dev
BUILD_PACKAGES += snmp
BUILD_PACKAGES += apache2-dev  # compiling mod_python
BUILD_PACKAGES += apache2      # compiling mod_python
BUILD_PACKAGES += libncurses5-dev # compiling mod-gearman
BUILD_PACKAGES += libpcap-dev # needed for CMC
BUILD_PACKAGES += gettext # needed for german l10n
BUILD_PACKAGES += libfreeradius-dev
#
# Check_MK build specific packages below
#
BUILD_PACKAGES += libgsf-1-dev # needed for msitools
BUILD_PACKAGES += librrd-dev # needed for CMC
BUILD_PACKAGES += libffi-dev # needed for pyOpenSSL (and dependant) compilations
BUILD_PACKAGES += libkrb5-dev # needed for python kerberos support
BUILD_PACKAGES += flex # needed for heirloom-pkgtools
BUILD_PACKAGES += openssh-client # needed for check_by_ssh
OS_PACKAGES     =
OS_PACKAGES    += time # needed for mk-job
OS_PACKAGES    += traceroute # needed for Check_MK parent scan
OS_PACKAGES    += curl
OS_PACKAGES    += dialog
OS_PACKAGES    += dnsutils
OS_PACKAGES    += fping
OS_PACKAGES    += graphviz
OS_PACKAGES    += apache2
OS_PACKAGES    += apache2-utils # contains htpasswd2
OS_PACKAGES    += libdbi1
OS_PACKAGES    += libevent-1.4-2
OS_PACKAGES    += libltdl7
OS_PACKAGES    += libnet-snmp-perl
OS_PACKAGES    += libpango1.0-0
OS_PACKAGES    += libperl5.26
OS_PACKAGES    += libreadline5
OS_PACKAGES    += libsnmp-perl
OS_PACKAGES    += libuuid1
OS_PACKAGES    += libxml2
OS_PACKAGES    += patch
OS_PACKAGES    += php-cli
OS_PACKAGES    += php-cgi
OS_PACKAGES    += php-gd
OS_PACKAGES    += php-mcrypt
OS_PACKAGES    += php-sqlite3
OS_PACKAGES    += php-json
OS_PACKAGES    += php-pear
OS_PACKAGES    += pyro
OS_PACKAGES    += rsync
OS_PACKAGES    += smbclient
OS_PACKAGES    += rpcbind # otherwise missing path in util.pm
OS_PACKAGES    += snmp
OS_PACKAGES    += unzip
OS_PACKAGES    += xinetd
OS_PACKAGES    += freeradius-utils
#
# Check_MK build specific packages below
#
OS_PACKAGES    += libpcap0.8 # needed for cmc
OS_PACKAGES    += rpm # needed by msitools/Agent Bakery
OS_PACKAGES    += binutils # needed by msitools/Agent Bakery
OS_PACKAGES    += lcab # needed for creating MSI packages
OS_PACKAGES    += libgsf-1-114 # needed by msitools/Agent Bakery
OS_PACKAGES    += libglib2.0-0 # needed by msitools/Agent Bakery
OS_PACKAGES    += cpio # needed for Agent bakery (solaris pkgs)
OS_PACKAGES    += poppler-utils # needed for preview of PDF in reporting
OS_PACKAGES     += libffi6 # needed for pyOpenSSL and dependant
USERADD_OPTIONS   =
ADD_USER_TO_GROUP = gpasswd -a %(user)s %(group)s
PACKAGE_INSTALL   = aptitude -y update ; aptitude -y install
ACTIVATE_INITSCRIPT = update-rc.d %s defaults
APACHE_CONF_DIR   = /etc/apache2/conf.d
APACHE_INIT_NAME  = apache2
APACHE_USER       = www-data
APACHE_GROUP      = www-data
APACHE_BIN        = /usr/sbin/apache2
APACHE_CTL        = /usr/sbin/apache2ctl
APACHE_MODULE_DIR = /usr/lib/apache2/modules
APACHE_MODULE_DIR_64 = /usr/lib/apache2/modules
HTPASSWD_BIN      = /usr/bin/htpasswd
APACHE_ENMOD      = a2enmod %s
PHP_FCGI_BIN      = /usr/bin/php-cgi
BECOME_ROOT       = sudo su -c
ARCH              = $(shell dpkg --print-architecture)
MOUNT_OPTIONS     =
INIT_CMD          = /etc/init.d/%(name)s %(action)s
