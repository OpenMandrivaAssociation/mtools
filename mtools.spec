%ifnarch %{riscv}
# (tpg) optimize it a bit
%global optflags %{optflags} -Oz --rtlib=compiler-rt
%endif

Summary:	Programs for accessing MS-DOS disks without mounting the disks
Name:		mtools
Version:	4.0.44
Release:	1
License:	GPLv3+
Group:		File tools
Url:		https://mtools.linux.lu
Source0:	http://mtools.linux.lu/%{name}-%{version}.tar.bz2
Patch0:		mtools-4.0.10-linux.patch
BuildSystem:	autotools
BuildOption:	--disable-floppyd

%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 Xdf disks, and 2m disks.

Mtools should be installed if you need to use MS-DOS disks.

%install -a
mkdir -p %{buildroot}%{_sysconfdir}
install -m644 mtools.conf %{buildroot}%{_sysconfdir}

%files
%config(noreplace) %{_sysconfdir}/mtools.conf
%doc COPYING NEWS README Release.notes mtools.texi
%{_bindir}/l*
%{_bindir}/m*
%{_bindir}/t*
%{_bindir}/u*
%{_bindir}/amuFormat.sh
%doc %{_mandir}/*/*
%doc %{_infodir}/%{name}.*
