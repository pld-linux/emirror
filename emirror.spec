Summary:	FTP mirroring program
Summary(pl):	Program do mirrorowania FTP
Name:		emirror
Version:	2.1.17
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://eclipt.uni-klu.ac.at:/pub/projects/emirror/%{name}-%{version}.tar.gz
Patch0:		%{name}-cfg.patch
BuildRequires:	python
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
%configure

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT%{_libdir}/emirror \
	etcdir=$RPM_BUILD_ROOT%{_sysconfdir}/emirror \
	docdir=$RPM_BUILD_ROOT%{_docdir}/emirror

(\
cd $RPM_BUILD_ROOT%{_bindir}; \
mv -f mirror mirror.bak; \
sed 's#@OUTPUTDIRECTORY@#/home/httpd/htdocs/mirrors#' mirror.bak > mirror; \
mv -f updateindex updateindex.bak; \
sed 's#@OUTPUTDIRECTORY@#/home/httpd/htdocs/mirrors#' updateindex.bak > updateindex;\
rm -f *.bak
)

install general.cfg $RPM_BUILD_ROOT%{_sysconfdir}/emirror

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
