Summary:	FTP mirroring program.
Summary(pl):	Program do mirrorowania FTP.
Name:		emirror
Version:	2.1.17
Release:	2
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Group(de):	Netzwerkwesen/Werkzeuge
Source0:	ftp://eclipt.uni-klu.ac.at/pub/projects/emirror/%{name}-%{version}.tar.gz
Patch0:		%{name}-pld.patch
BuildRequires:	python-devel
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTP mirroring program.

%description -l pl
Program do mirrorowania FTP.

%prep
%setup -q
%patch -p1

%build
autoconf
%configure \
	--with-htmldir=/home/httpd/html

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf doc/* $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%config(noreplace) %{_sysconfdir}/emirror
%attr(755,root,root) %{_bindir}/*
%{_libdir}/emirror
%{_mandir}/man1/*
