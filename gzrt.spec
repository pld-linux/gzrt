Summary:	gzip recovery toolkit
Summary(pl.UTF-8):	Zestaw naprawczy do gzipa
Name:		gzrt
Version:	0.6
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://www.urbanophile.com/arenn/hacking/gzrt/%{name}-%{version}.tar.gz
# Source0-md5:	c4df7186da77d8d7ff9041cc4c7fd37a
URL:		http://www.urbanophile.com/arenn/hacking/gzrt/gzrt.html
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gzip recovery toolkit attempts to automate the recovery of data
from corrupted gzip files through a program called gzrecover.  This
package is very experimental at this point.

%description -l pl.UTF-8
gzrt próbuje zautomatyzować odtwarzanie danych z uszkodzonych archiwów
gzip z użyciem programu gzrecover. To narzędzie należy jeszcze
traktować jako eksperymentalne.

%prep
%setup -q

%build
%{__cc} %{rpmldflags} %{rpmcflags} %{rpmcppflags} -o gzrecover \
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
%attr(755,root,root) %{_bindir}/gzrecover
