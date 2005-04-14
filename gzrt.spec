Summary:	gzip recovery toolkit
Summary(pl):	Zestaw naprawczy do gzipa
Name:		gzrt
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.urbanophile.com/arenn/hacking/gzrt/%{name}-%{version}.tar.gz
# Source0-md5:	b54888d4b7a0f130dec89e477b091159
URL:		http://www.urbanophile.com/arenn/hacking/gzrt/gzrt.html
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gzip recovery toolkit attempts to automate the recovery of data
from corrupted gzip files through a program called gzrecover.  This
package is very experimental at this point.

%description -l pl
gzrt próbuje zautomatyzowaæ odtwarzanie danych z uszkodzonych archiwów
gzip z u¿yciem programu gzrecover. To narzêdzie nale¿y jeszcze
traktowaæ jako eksperymentalne.

%prep
%setup -q

%build
%{__cc} %{rpmldflags} %{rpmcflags} -o gzrecover \
	-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 gzrecover.c -lz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install gzrecover $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
