Summary:     FTP mirroring program.
Summary(pl): Program do mirrorowania FTP.
Name:        emirror
Version:     2.0b6
Release:     1
Copyright:   GPL
Source:      ftp://ftp.uni-klu.ac.at/pub/projects/emirror/%{name}-%{version}.tar.gz
Patch:	     emirror.cfg.diff
Group:       Networking/Utilities
Group(pl):   Sieæ/Narzêdzia
BuildRoot:   /tmp/%{name}-%{version}-root
Requires:    python
BuildArch:   noarch

%description
FTP mirroring program.

%description -l pl
Program do mirrorowania FTP.

%prep
%setup -q
%patch -p1

%build
./configure --prefix=/usr

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	bindir=$RPM_BUILD_ROOT/usr/bin \
	libdir=$RPM_BUILD_ROOT/usr/lib/emirror \
	etcdir=$RPM_BUILD_ROOT/etc/emirror \
	docdir=$RPM_BUILD_ROOT/usr/doc/emirror

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc documentation/* html README scripts/mirror
%attr(755, root, root) /usr/bin/emconvert
%attr(755, root, root) /usr/bin/emirror
/usr/lib/emirror

%changelog
* Sat Dec 05 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [2.0b6-1]
- initial rpm release.
