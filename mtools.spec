%ifnarch %{riscv}
# (tpg) optimize it a bit
%global optflags %{optflags} -Oz --rtlib=compiler-rt
%endif

Summary:	Programs for accessing MS-DOS disks without mounting the disks
Name:		mtools
Version:	4.0.43
Release:	2
License:	GPLv3+
Group:		File tools
Url:		http://mtools.linux.lu
Source0:	http://mtools.linux.lu/%{name}-%{version}.tar.bz2
Patch0:		mtools-4.0.10-linux.patch

%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 Xdf disks, and 2m disks.

Mtools should be installed if you need to use MS-DOS disks.

%prep
%autosetup -p1

%build
%configure --disable-floppyd
%make_build

%install
mkdir -p %{buildroot}/%{_prefix} %{buildroot}%{_sysconfdir}
%make_install

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
