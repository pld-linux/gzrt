Summary:	gzip recovery toolkit
Summary(pl):	zestaw naprawczy do gzipa
Name:		gzrt
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.urbanophile.com/arenn/hacking/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	261a337ba26dd29104083ccf69fbe4ce
URL:		http://www.urbanophile.com/arenn/hacking/gzrt/gzrt.html
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gzip Recovery Toolkit attempts to automate the recovery of data from
corrupted gzip files through a program called gzrecover. This package is
very experimental at this point.

%description -l pl
gzrt próbuje zautomatyzowaæ odtwarzanie danych z uszkodzonych archiwów gzip
z u¿yciem programu gzrecover. To narzêdzie nale¿y jeszcze traktowaæ jako
eksperymentalne.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_bindir}

install gzrecover $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
