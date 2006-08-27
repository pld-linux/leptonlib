Summary:	Leptonica - image processing and analysis library
Summary(pl):	Leptonica - biblioteka do przetwarzania i analizy obrazu
Name:		leptonlib
Version:	1.38
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.leptonica.com/source/%{name}-%{version}.tar.gz
# Source0-md5:	b466a01524bf1b523f1c933d7d6e7b3f
Patch0:		%{name}-link.patch
URL:		http://www.leptonica.com/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Leptonica - image processing and analysis library.

%description -l pl
Leptonica - biblioteka do przetwarzania i analizy obrazu.

%package devel
Summary:	Header files for lepton library
Summary(pl):	Pliki nag³ówkowe biblioteki lepton
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel

%description devel
Header files for lepton library.

%description devel -l pl
Pliki nag³ówkowe biblioteki lepton.

%package static
Summary:	Static lepton library
Summary(pl):	Statyczna biblioteka lepton
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lepton library.

%description static -l pl
Statyczna biblioteka lepton.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C src nodebug \
	CC="%{__cc} -ansi -DANSI -D_BSD_SOURCE" \
	OPTIMIZE="%{rpmcflags}"

%{__make} -C src shared \
	CC="%{__cc} -ansi -DANSI -D_BSD_SOURCE" \
	LIBRARIAN_SHARED="%{__cc} -shared" \
	OPTIMIZE="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}" \
	SHARED=yes

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/lept,%{_libdir}}

install lib/nodebug/liblept.a $RPM_BUILD_ROOT%{_libdir}
cp -af lib/shared/liblept.so* $RPM_BUILD_ROOT%{_libdir}
install src/*.h $RPM_BUILD_ROOT%{_includedir}/lept

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html library-notes.txt version-notes.html
%attr(755,root,root) %{_libdir}/liblept.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblept.so
%{_includedir}/lept

%files static
%defattr(644,root,root,755)
%{_libdir}/liblept.a
