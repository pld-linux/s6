#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

Summary:	skarnet.org's small and secure supervision software suite
Name:		s6
Version:	2.3.0.0
Release:	0.1
License:	ISC license
Group:		Networking/Admin
Source0:	http://www.skarnet.org/software/s6/%{name}-%{version}.tar.gz
# Source0-md5:	e5c01be33a0cb6cbc76bd4382f94452f
URL:		http://www.skarnet.org/software/s6/
BuildRequires:	execline-devel >= 2.1.5.0
BuildRequires:	make >= 3.81
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	skalibs-devel >= 2.3.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
s6 is a small suite of programs for UNIX, designed to allow process
supervision (a.k.a service supervision), in the line of daemontools
and runit.

%package devel
Summary:	Header files and development documentation for s6
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for s6.

%package doc
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Podręcznik dla %{name}
Group:		Documentation
# noarch subpackages only when building with rpm5
BuildArch:	noarch

%description doc
Documentation for %{name}.

%description doc -l fr.UTF-8
Documentation pour %{name}.

%description doc -l it.UTF-8
Documentazione di %{name}.

%description doc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q

sed -i "s~tryldflag LDFLAGS_AUTO -Wl,--hash-style=both~:~" configure

%build
%configure \
	--enable-shared \
	--disable-static \
	--disable-allstatic \
	--bindir=%{_sbindir} \
	--sbindir=%{_sbindir} \
	--dynlibdir=%{_libdir} \
	--libdir=%{_libdir} \
	--datadir=%{_sysconfdir} \
	--sysdepdir=%{_libdir}/skalibs \
	--dynlibdir=%{_libdir} \
	--with-sysdeps=%{_libdir}/skalibs \
	%{nil}

%if 0
echo "%{__cc} %{rpmcflags} -Wall" > conf-compile/conf-cc
echo "%{__cc} %{rpmldflags}" > conf-compile/conf-ld
echo "%{__cc} %{rpmldflags}" > conf-compile/conf-dynld
echo %{_libdir}/%{name} > conf-compile/conf-install-library
echo %{_libdir} > conf-compile/conf-install-library.so
echo > conf-compile/conf-stripbins
echo > conf-compile/conf-striplibs
rm conf-compile/flag-slashpackage
echo %{_libdir}/skalibs/sysdeps > conf-compile/import
echo %{_includedir}/skalibs > conf-compile/path-include
echo %{_includedir} >> conf-compile/path-include
echo %{_libdir}/skalibs > conf-compile/path-library
echo %{_libdir} >> conf-compile/path-library
echo %{_libdir}/skalibs > conf-compile/path-library.so
echo %{_libdir} >> conf-compile/path-library.so
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# SONAME: libs6.so.2.3
# so this is junk
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libs6.so.2.3.0

%if 0
install -p command/* $RPM_BUILD_ROOT%{_sbindir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/s6-accessrules-cdb-from-fs
%attr(755,root,root) %{_sbindir}/s6-accessrules-fs-from-cdb
%attr(755,root,root) %{_sbindir}/s6-applyuidgid
%attr(755,root,root) %{_sbindir}/s6-cleanfifodir
%attr(755,root,root) %{_sbindir}/s6-connlimit
%attr(755,root,root) %{_sbindir}/s6-envdir
%attr(755,root,root) %{_sbindir}/s6-envuidgid
%attr(755,root,root) %{_sbindir}/s6-fdholder-daemon
%attr(755,root,root) %{_sbindir}/s6-fdholder-delete
%attr(755,root,root) %{_sbindir}/s6-fdholder-deletec
%attr(755,root,root) %{_sbindir}/s6-fdholder-getdump
%attr(755,root,root) %{_sbindir}/s6-fdholder-getdumpc
%attr(755,root,root) %{_sbindir}/s6-fdholder-list
%attr(755,root,root) %{_sbindir}/s6-fdholder-listc
%attr(755,root,root) %{_sbindir}/s6-fdholder-retrieve
%attr(755,root,root) %{_sbindir}/s6-fdholder-retrievec
%attr(755,root,root) %{_sbindir}/s6-fdholder-setdump
%attr(755,root,root) %{_sbindir}/s6-fdholder-setdumpc
%attr(755,root,root) %{_sbindir}/s6-fdholder-store
%attr(755,root,root) %{_sbindir}/s6-fdholder-storec
%attr(755,root,root) %{_sbindir}/s6-fdholder-transferdump
%attr(755,root,root) %{_sbindir}/s6-fdholder-transferdumpc
%attr(755,root,root) %{_sbindir}/s6-fdholderd
%attr(755,root,root) %{_sbindir}/s6-fghack
%attr(755,root,root) %{_sbindir}/s6-ftrig-listen
%attr(755,root,root) %{_sbindir}/s6-ftrig-listen1
%attr(755,root,root) %{_sbindir}/s6-ftrig-notify
%attr(755,root,root) %{_sbindir}/s6-ftrig-wait
%attr(755,root,root) %{_sbindir}/s6-ftrigrd
%attr(755,root,root) %{_sbindir}/s6-ioconnect
%attr(755,root,root) %{_sbindir}/s6-ipcclient
%attr(755,root,root) %{_sbindir}/s6-ipcserver
%attr(755,root,root) %{_sbindir}/s6-ipcserver-access
%attr(755,root,root) %{_sbindir}/s6-ipcserver-socketbinder
%attr(755,root,root) %{_sbindir}/s6-ipcserverd
%attr(755,root,root) %{_sbindir}/s6-log
%attr(755,root,root) %{_sbindir}/s6-mkfifodir
%attr(755,root,root) %{_sbindir}/s6-setlock
%attr(755,root,root) %{_sbindir}/s6-setsid
%attr(755,root,root) %{_sbindir}/s6-setuidgid
%attr(755,root,root) %{_sbindir}/s6-softlimit
%attr(755,root,root) %{_sbindir}/s6-sudo
%attr(755,root,root) %{_sbindir}/s6-sudoc
%attr(755,root,root) %{_sbindir}/s6-sudod
%attr(755,root,root) %{_sbindir}/s6-supervise
%attr(755,root,root) %{_sbindir}/s6-svc
%attr(755,root,root) %{_sbindir}/s6-svlisten
%attr(755,root,root) %{_sbindir}/s6-svlisten1
%attr(755,root,root) %{_sbindir}/s6-svok
%attr(755,root,root) %{_sbindir}/s6-svscan
%attr(755,root,root) %{_sbindir}/s6-svscanctl
%attr(755,root,root) %{_sbindir}/s6-svstat
%attr(755,root,root) %{_sbindir}/s6-svwait
%attr(755,root,root) %{_sbindir}/s6-tai64n
%attr(755,root,root) %{_sbindir}/s6-tai64nlocal
%attr(755,root,root) %{_sbindir}/s6lockd
%attr(755,root,root) %{_sbindir}/ucspilogd

%attr(755,root,root) %{_libdir}/s6lockd-helper

# -libs
%attr(755,root,root) %{_libdir}/libs6.so.*.*.*.*
%ghost %{_libdir}/libs6.so.2.3

%files devel
%defattr(644,root,root,755)
%{_includedir}/s6
%{_libdir}/libs6.so

%files doc
%defattr(644,root,root,755)
%doc doc/*
%{_examplesdir}/%{name}-%{version}
