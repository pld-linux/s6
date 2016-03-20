Summary:	skarnet.org's small and secure supervision software suite
Name:		s6
Version:	1.1.1
Release:	1
License:	ISC license
Group:		Networking/Admin
Source0:	http://www.skarnet.org/software/s6/%{name}-%{version}.tar.gz
# Source0-md5:	a4fc19506284c79851d6de4a35275c07
URL:		http://www.skarnet.org/software/s6/
BuildRequires:	execline >= 1.2.2
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	skalibs >= 1.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
s6 is a small suite of programs for UNIX, designed to allow process
supervision (a.k.a service supervision), in the line of daemontools
and runit.

%package doc
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Podręcznik dla %{name}
Group:		Documentation
# noarch subpackages only when building with rpm5
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Documentation for %{name}.

%description doc -l fr.UTF-8
Documentation pour %{name}.

%description doc -l it.UTF-8
Documentazione di %{name}.

%description doc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -qc
mv admin/%{name}-%{version}/* .

%build
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

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_examplesdir}/%{name}-%{version}}

install -p command/* $RPM_BUILD_ROOT%{_sbindir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/s6-cleanfifodir
%attr(755,root,root) %{_sbindir}/s6-envdir
%attr(755,root,root) %{_sbindir}/s6-envuidgid
%attr(755,root,root) %{_sbindir}/s6-fghack
%attr(755,root,root) %{_sbindir}/s6-ftrig-listen
%attr(755,root,root) %{_sbindir}/s6-ftrig-listen1
%attr(755,root,root) %{_sbindir}/s6-ftrig-notify
%attr(755,root,root) %{_sbindir}/s6-ftrig-wait
%attr(755,root,root) %{_sbindir}/s6-ftrigrd
%attr(755,root,root) %{_sbindir}/s6-log
%attr(755,root,root) %{_sbindir}/s6-mkfifodir
%attr(755,root,root) %{_sbindir}/s6-setlock
%attr(755,root,root) %{_sbindir}/s6-setsid
%attr(755,root,root) %{_sbindir}/s6-setuidgid
%attr(755,root,root) %{_sbindir}/s6-softlimit
%attr(755,root,root) %{_sbindir}/s6-supervise
%attr(755,root,root) %{_sbindir}/s6-svc
%attr(755,root,root) %{_sbindir}/s6-svok
%attr(755,root,root) %{_sbindir}/s6-svscan
%attr(755,root,root) %{_sbindir}/s6-svscanctl
%attr(755,root,root) %{_sbindir}/s6-svstat
%attr(755,root,root) %{_sbindir}/s6-svwait
%attr(755,root,root) %{_sbindir}/s6-tai64n
%attr(755,root,root) %{_sbindir}/s6-tai64nlocal
%attr(755,root,root) %{_sbindir}/s6lockd
%attr(755,root,root) %{_sbindir}/s6lockd-helper
%attr(755,root,root) %{_sbindir}/ucspilogd

%files doc
%defattr(644,root,root,755)
%doc doc/*
%{_examplesdir}/%{name}-%{version}
