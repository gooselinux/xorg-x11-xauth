%define pkgname xauth

Summary: X.Org X11 X authority utilities
Name: xorg-x11-%{pkgname}
Version: 1.0.2
Release: 7.1%{?dist}
# NOTE: Remove Epoch line if package gets renamed
Epoch: 1
License: MIT
Group: User Interface/X
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: ftp://ftp.x.org/pub/individual/app/%{pkgname}-%{version}.tar.bz2
Source10: mkxauth
Source11: mkxauth.man

BuildRequires: pkgconfig
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libXext-devel
BuildRequires: libXmu-devel

Provides: xauth
Provides: mkxauth

Obsoletes: XFree86-xauth, mkxauth

# NOTE: xauth moved from the XFree86 package to XFree86-xauth in
# XFree86-4.2.0-50.11, so this Obsoletes line is required for upgrades
# from RHL 8 and older, and RHEL 2.1 to work properly when upgrading to
# a newer OS release.
Obsoletes: XFree86 < 4.2.0-50.11

%description
xauth is used to edit and display the authorization information
used in connecting to an X server.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
# Install mkxauth
{
   install -m 755 %{SOURCE10} $RPM_BUILD_ROOT%{_bindir}/
   install -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_mandir}/man1/mkxauth.1x
}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/xauth
%{_bindir}/mkxauth
#%dir %{_mandir}/man1x
%{_mandir}/man1/xauth.1*
%{_mandir}/man1/mkxauth.1*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1:1.0.2-7.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.0.2-5
- Fix license tag

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:1.0.2-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1:1.0.2-3
- Rebuild for build id

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 1:1.0.2-2
- Don't install INSTALL

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 1:1.0.2-1.fc7
- Update to 1.0.2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Wed Jun 21 2006 Mike A. Harris <mharris@redhat.com> 1:1.0.1-2
- Add missing documentation to doc manifest.
- Use "make install" instead of makeinstall macro.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1:1.0.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1:1.0.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1:1.0.1-1
- Updated to xauth 1.0.1 from X11R7.0

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1:1.0.0-1
- Updated to xauth 1.0.0 from X11R7 RC4
- Changed manpage dir from man1x to man1 to match upstream default.

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 1:0.99.2-1
- Updated to xauth 0.99.2 from X11R7 RC2
- Added Epoch 1 to package, to be able to change the version number from the
  X11R7 release number to the actual twm version.
- Rename mkxauth manpage to mkxauth.1x

* Mon Oct 31 2005 Mike A. Harris <mharris@redhat.com> 6.99.99.0-3
- Updated to xauth 0.99.1 from X11R7 RC1
- Change manpage location to 'man1x' in file manifest

* Wed Aug 24 2005 Mike A. Harris <mharris@redhat.com> 6.99.99.0-2
- Use Fedora-Extras style BuildRoot tag
- Update BuildRequires to use new library package names

* Wed Aug 24 2005 Mike A. Harris <mharris@redhat.com> 6.99.99.0-1
- Initial build.
