Summary:	FTP mirroring program
Summary(pl):	Program do mirrorowania FTP
Name:		emirror
Version:	2.1.19
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://eclipt.uni-klu.ac.at/pub/projects/emirror/%{name}-%{version}.tar.gz
Patch0:		%{name}-pld.patch
BuildRequires:	python-devel
Requires:	python >= 2.0
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
%configure2_13 \
	--with-htmldir=/home/httpd/html/mirrors

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/httpd/html/mirrors

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf doc/* $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%dir /home/httpd/html/mirrors
/home/httpd/html/mirrors/*
%config(noreplace) %{_sysconfdir}/emirror
%attr(755,root,root) %{_bindir}/*
%{_libdir}/emirror
%{_mandir}/man1/*
