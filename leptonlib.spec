Summary:	Leptonica - image processing and analysis library
Summary(pl.UTF-8):	Leptonica - biblioteka do przetwarzania i analizy obrazu
Name:		leptonlib
Version:	1.74.4
Release:	1
License:	BSD-like
Group:		Libraries
#Source0Download: http://www.leptonica.com/download.html
Source0:	http://www.leptonica.com/source/leptonica-%{version}.tar.gz
# Source0-md5:	4f32be9bd2e2c142ba018037ab5d746f
URL:		http://www.leptonica.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	giflib-devel >= 5
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libwebp-devel
BuildRequires:	openjpeg2-devel >= 2
BuildRequires:	zlib-devel
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
Requires:	giflib-devel >= 5
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel
Requires:	libwebp-devel
Requires:	zlib-devel

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
%setup -q -n leptonica-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# programs are mostly examples or tests (seems nothing really useful)
# and they have too generic names
%configure \
	--disable-programs \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblept.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html leptonica-license.txt version-notes.html moller52.jpg
%attr(755,root,root) %{_libdir}/liblept.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblept.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblept.so
%{_includedir}/leptonica
%{_pkgconfigdir}/lept.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblept.a
