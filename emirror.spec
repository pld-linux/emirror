Summary:	FTP mirroring program
Summary(pl):	Program do mirrorowania FTP
Name:		emirror
Version:	2.1.21
Release:	4
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://eclipt.uni-klu.ac.at/pub/projects/emirror/%{name}-%{version}.tar.gz
# Source0-md5:	4223966e49284e70a8eeabe9603d1ae3
Patch0:		%{name}-pld.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fhs-compliance
BuildRequires:	python-devel >= 2.1
Requires:	python >= 2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTP mirroring program.

%description -l pl
Program do mirrorowania FTP.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-htmldir=/srv/httpd/html/mirrors

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/srv/httpd/html/mirrors

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%dir /srv/httpd/html/mirrors
/srv/httpd/html/mirrors/*
%config(noreplace) %{_sysconfdir}/emirror
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/emirror
%{_mandir}/man1/*
