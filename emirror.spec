Summary:	FTP mirroring program.
Summary(pl):	Program do mirrorowania FTP.
Name:		emirror
Version:	2.1
Release:	1pre9
Copyright:	GPL
Source:		ftp://ftp.uni-klu.ac.at/pub/projects/emirror/%{name}-%{version}-pre9.tar.bz2
Patch:		emirror-cfg.patch
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	python
BuildArch:	noarch

%description
FTP mirroring program.

%description -l pl
Program do mirrorowania FTP.

%prep
%setup -q -n %{name}-%{version}-pre9
%patch -p1

%build
./configure --prefix=/usr

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT%{_libdir}/emirror \
	etcdir=$RPM_BUILD_ROOT/etc/emirror \
	docdir=$RPM_BUILD_ROOT%{_docdir}/emirror

(\
cd $RPM_BUILD_ROOT%{_bindir}; \
mv -f mirror mirror.bak; \
sed 's#@OUTPUTDIRECTORY@#/home/httpd/htdocs/mirrors#' mirror.bak > mirror; \
mv -f updateindex updateindex.bak; \
sed 's#@OUTPUTDIRECTORY@#/home/httpd/htdocs/mirrors#' updateindex.bak > updateindex;\
rm -f *.bak
)

install general.cfg $RPM_BUILD_ROOT/etc/emirror

gzip -9nf doc/* Readme $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* Readme.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/emirror
%{_mandir}/man1/*
