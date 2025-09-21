#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Leptonica - image processing and analysis library
Summary(pl.UTF-8):	Leptonica - biblioteka do przetwarzania i analizy obrazu
Name:		leptonlib
Version:	1.84.1
Release:	2
License:	BSD-like
Group:		Libraries
#Source0Download: http://www.leptonica.org/download.html
Source0:	http://www.leptonica.org/source/leptonica-%{version}.tar.gz
# Source0-md5:	01e6de7af2ba93b8350cdc3f7aeb0fbf
URL:		http://www.leptonica.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	giflib-devel >= 5.1.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libtool >= 2:2
BuildRequires:	libwebp-devel >= 0.5.0
BuildRequires:	openjpeg2-devel >= 2.1.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	zlib-devel
Requires:	giflib >= 5.1.3
Requires:	libwebp >= 0.5.0
Requires:	openjpeg2 >= 2.1.0
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
Requires:	giflib-devel >= 5.1.3
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel >= 4
Requires:	libwebp-devel >= 0.5.0
Requires:	openjpeg2-devel >= 2.1.0
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
	--disable-silent-rules \
	%{__enable_disable static_libs static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblept*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html leptonica-license.txt version-notes.html moller52.jpg
%attr(755,root,root) %{_libdir}/libleptonica.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libleptonica.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libleptonica.so
%{_includedir}/leptonica
%{_pkgconfigdir}/lept.pc
%{_libdir}/cmake/LeptonicaConfig*.cmake

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libleptonica.a
%endif
