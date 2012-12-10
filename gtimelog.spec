Summary: a small application to keep track of your time
Name: gtimelog
Version: 0.5.0
Release: 2
Group: Office
License: GPLv2
URL: http://mg.pov.lt/gtimelog/
Source0: http://pypi.python.org/packages/source/g/%name/%name-%version.tar.gz
Requires: pygtk2.0
Requires: pygtk2.0-libglade
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: desktop-file-utils

%description
GTimeLog is a small Gtk+ app for keeping track of your time. It's main goal
is to be as unintrusive as possible.

%prep
%setup -q

%build

%install
%__rm -rf %buildroot
%__python setup.py install --root=%buildroot
mkdir -p %buildroot%_datadir/applications
desktop-file-install \
        --dir %buildroot%_datadir/applications \
        %name.desktop

%files
%doc README.txt NEWS.txt gtimelogrc.example
%attr(0755,root,root)%_bindir/%name
%py_sitedir/%{name}*
%_datadir/applications/%name.desktop


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 645232
- update to new version 0.5.0

* Sat Nov 06 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0.4.0-1mdv2011.0
+ Revision: 594262
- imported package gtimelog

