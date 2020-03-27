Summary:	NTFS-3G plugin for reading "system compressed" files
Name:		ntfs-3g-system-compression
Version:	1.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		https://github.com/ebiggers/ntfs-3g-system-compression
Source0:	https://github.com/ebiggers/ntfs-3g-system-compression/archive/v%{version}/ntfs-3g-system-compression-%{version}.tar.gz
BuildRequires:	pkgconfig(libntfs-3g) >= 2017.3.23
BuildRequires:	pkgconfig(fuse)

%description
System compression, also known as "Compact OS", is a Windows feature that
allows rarely modified files to be compressed using the XPRESS or LZX
compression formats. It is not built directly into NTFS but rather is
implemented using reparse points. This feature appeared in Windows 10 and it
appears that many Windows 10 systems have been using it by default.

This RPM contains a plugin which enables the NTFS-3G FUSE driver to
transparently read from system-compressed files. Currently, only reading is
supported. Compressing an existing file may be done by using the "compact"
utility on Windows.

%prep
%autosetup -p1

%build
autoreconf -i
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_libdir}/ntfs-3g/*.la

%files
%doc README.md
%license COPYING
%dir %{_libdir}/ntfs-3g/
%{_libdir}/ntfs-3g/ntfs-plugin-80000017.so
