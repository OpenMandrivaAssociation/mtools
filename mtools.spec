Summary:	Programs for accessing MS-DOS disks without mounting the disks
Name:		mtools
Version:	4.0.17
Release:	9
License:	GPLv3+
Group:		File tools
Url:		http://mtools.linux.lu
Source0:	http://mtools.linux.lu/%{name}-%{version}.tar.bz2
Source1:	69-floppy-acl.rules
Patch0:		mtools-4.0.10-linux.patch
Patch1:		mtools-4.0.12-atari.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xau)

%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 Xdf disks, and 2m disks.

Mtools should be installed if you need to use MS-DOS disks.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
mkdir -p %{buildroot}/%{_prefix} %{buildroot}%{_sysconfdir}
%makeinstall_std
install mtools.conf %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/%{_sysconfdir}/udev/rules.d/
install -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/udev/rules.d/69-floppy-acl.rules

%files
%{_sysconfdir}/udev/rules.d/*.rules
%config(noreplace) %{_sysconfdir}/mtools.conf
%doc COPYING NEWS README Release.notes mtools.texi
%{_bindir}/f*
%{_bindir}/l*
%{_bindir}/m*
%{_bindir}/t*
%{_bindir}/u*
%{_bindir}/amuFormat.sh
%{_mandir}/*/*
%{_infodir}/%{name}.*

