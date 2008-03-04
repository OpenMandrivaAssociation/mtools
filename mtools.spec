Summary:	Programs for accessing MS-DOS disks without mounting the disks
Name: 		mtools
Version: 	3.9.11
Release: 	%mkrel 3
License: 	GPL
Group: 		File tools
Url: 		http://mtools.linux.lu
Source: 	http://mtools.linux.lu/%{name}-%{version}.tar.bz2
Patch0: 	mtools-3.9.1-linux.patch
Patch2: 	mtools-3.9.6-atari.patch
Patch4: 	mtools-3.9.8-fs.patch
Patch5: 	mtools-3.9.9-supermount.patch
BuildRequires: 	X11-devel
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
%patch2 -p1 -b .atari
%patch4 -p1 -b .compil
%patch5 -p1 -b .supermount

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_prefix} %{buildroot}%{_sysconfdir}
%makeinstall
install mtools.conf %{buildroot}%{_sysconfdir}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/mtools.conf
%doc COPYING Changelog README Release.notes mtools.texi
%attr(755,root,root) %{_bindir}/f*
%attr(755,root,root) %{_bindir}/l*
%attr(755,root,root) %{_bindir}/m*
%attr(755,root,root) %{_bindir}/t*
%attr(755,root,root) %{_bindir}/u*
%attr(755,root,root) %{_bindir}/amuFormat.sh
%{_mandir}/*/*
%{_infodir}/%{name}.*


