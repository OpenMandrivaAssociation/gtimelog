Summary: a small application to keep track of your time
Name: gtimelog
Version: 0.4.0
Release: %mkrel 1
Group: Office
License: GPLv2
URL: http://mg.pov.lt/gtimelog/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0: http://pypi.python.org/packages/source/g/%name/%name-%version.tar.gz
Requires: pygtk2.0
Requires: pygtk2.0-libglade
BuildRequires: libpython-devel
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
