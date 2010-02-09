Summary:	Leptonica - image processing and analysis library
Summary(pl.UTF-8):	Leptonica - biblioteka do przetwarzania i analizy obrazu
Name:		leptonlib
Version:	1.57
Release:	4
License:	BSD-like
Group:		Libraries
Source0:	http://www.leptonica.com/source/%{name}-%{version}.tar.gz
# Source0-md5:	4c0deb5b18765e9db2dd675c5fb47d08
Patch0:		%{name}-shared.patch
Patch1:		%{name}-endiantest.patch
URL:		http://www.leptonica.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	giflib-devel >= 4
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Leptonica - image processing and analysis library.

%description -l pl.UTF-8
Leptonica - biblioteka do przetwarzania i analizy obrazu.

%package devel
Summary:	Header files for lepton library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lepton
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	giflib-devel >= 4
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel

%description devel
Header files for lepton library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lepton.

%package static
Summary:	Static lepton library
Summary(pl.UTF-8):	Statyczna biblioteka lepton
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lepton library.

%description static -l pl.UTF-8
Statyczna biblioteka lepton.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/lept,%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html leptonica-license.txt version-notes.html moller52.jpg
%attr(755,root,root) %{_libdir}/liblept.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liblept.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblept.so
%{_libdir}/liblept.la
%{_includedir}/liblept

%files static
%defattr(644,root,root,755)
%{_libdir}/liblept.a
