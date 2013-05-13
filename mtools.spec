Summary:	Programs for accessing MS-DOS disks without mounting the disks
Name: 		mtools
Version: 	4.0.17
Release: 	3
License: 	GPLv3+
Group: 		File tools
Url: 		http://mtools.linux.lu
Source: 	http://mtools.linux.lu/%{name}-%{version}.tar.bz2
Source1:	69-floppy-acl.rules
Patch0: 	mtools-4.0.10-linux.patch
Patch2: 	mtools-4.0.12-atari.patch
BuildRequires: 	pkgconfig(x11)
BuildRequires:	pkgconfig(xau)
BuildRequires:	texinfo

%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 Xdf disks, and 2m disks.

Mtools should be installed if you need to use MS-DOS disks.

%prep
%setup -q
%patch0 -p1 
%patch2 -p0  

%build
%configure2_5x
%make

%install
mkdir -p %{buildroot}/%{_prefix} %{buildroot}%{_sysconfdir}
%makeinstall
install mtools.conf %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/%{_sysconfdir}/udev/rules.d/
install -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/udev/rules.d/69-floppy-acl.rules

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


%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Wed Jun 29 2011 Sandro Cazzaniga <kharec@mandriva.org> 4.0.17-1mdv2011.0
+ Revision: 688193
- fix patch macros
- new version 4.0.17

* Sun Apr 17 2011 Sandro Cazzaniga <kharec@mandriva.org> 4.0.16-1
+ Revision: 654129
- new version

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 4.0.15-2
+ Revision: 636298
- rebuild
- tighten BR

* Tue Nov 23 2010 Eugeni Dodonov <eugeni@mandriva.com> 4.0.15-1mdv2011.0
+ Revision: 600272
- Updated to 4.0.15.

* Sun Oct 17 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.0.14-1mdv2011.0
+ Revision: 586252
- update to new version 4.0.14

* Mon Mar 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.0.13-1mdv2010.1
+ Revision: 512978
- up to 4.0.13

* Fri Jan 15 2010 Emmanuel Andry <eandry@mandriva.org> 4.0.12-1mdv2010.1
+ Revision: 491841
- New version 4.0.12
- rediff p2

* Tue Oct 27 2009 Frederic Crozat <fcrozat@mandriva.com> 4.0.10-3mdv2010.0
+ Revision: 459472
- Add udev ACL for floppy access for non-root users (Mdv bug #39916)

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.0.10-2mdv2010.0
+ Revision: 426199
- rebuild

* Wed Mar 18 2009 Nicolas Vigier <nvigier@mandriva.com> 4.0.10-1mdv2009.1
+ Revision: 357451
- version 4.0.10
- rediff patch0
- drop patch3 (applied upstream)

* Wed Jan 14 2009 Frederic Crozat <fcrozat@mandriva.com> 4.0.1-2mdv2009.1
+ Revision: 329549
- Remove patch5, supermount is dead
- Patch3: fix buffer overflow detected by fortify

* Sun Dec 28 2008 Oden Eriksson <oeriksson@mandriva.com> 4.0.1-1mdv2009.1
+ Revision: 320312
- 4.0.1
- rediffed one fuzzy patch

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.9.11-5mdv2009.0
+ Revision: 223327
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3.9.11-4mdv2008.1
+ Revision: 180102
- bump release
- drop P4 to make it compile
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jul 07 2007 Nicolas Vigier <nvigier@mandriva.com> 3.9.11-1mdv2008.0
+ Revision: 49606
- new version
- drop useless old patch


* Sun Feb 11 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.9.10-3mdv2007.0
+ Revision: 118825
- Import mtools

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.9.10-2mdk
- Rebuild

* Tue Jul 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.9.10-1mdk
- New release 3.9.10

* Fri Feb 20 2004 Vincent Danen <vdanen@mandrakesoft.com> 3.9.9-3mdk
- undo the special-but-insecure handling for mformat (aka no more suid)

