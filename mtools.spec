Summary:	Programs for accessing MS-DOS disks without mounting the disks
Name: 		mtools
Version: 	4.0.15
Release: 	%mkrel 1
License: 	GPLv3+
Group: 		File tools
Url: 		http://mtools.linux.lu
Source: 	http://mtools.linux.lu/%{name}-%{version}.tar.bz2
Source1:	69-floppy-acl.rules
Patch0: 	mtools-4.0.10-linux.patch
Patch2: 	mtools-4.0.12-atari.patch
BuildRequires: 	libx11-devel
BuildRequires:	libxau-devel
BuildRequires:	texinfo
Requires(pre): 	info-install
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 Xdf disks, and 2m disks.

Mtools should be installed if you need to use MS-DOS disks.

%prep
%setup -q
%patch0 -p1 -b .linux
%patch2 -p0 -b .atari

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_prefix} %{buildroot}%{_sysconfdir}
%makeinstall
install mtools.conf %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/%{_sysconfdir}/udev/rules.d/
install -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/udev/rules.d/69-floppy-acl.rules

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(644,root,root,755)
%{_sysconfdir}/udev/rules.d/*.rules
%config(noreplace) %{_sysconfdir}/mtools.conf
%doc COPYING NEWS README Release.notes mtools.texi
%attr(755,root,root) %{_bindir}/f*
%attr(755,root,root) %{_bindir}/l*
%attr(755,root,root) %{_bindir}/m*
%attr(755,root,root) %{_bindir}/t*
%attr(755,root,root) %{_bindir}/u*
%attr(755,root,root) %{_bindir}/amuFormat.sh
%{_mandir}/*/*
%{_infodir}/%{name}.*


