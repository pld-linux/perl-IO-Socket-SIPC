#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	IO
%define	pnam	Socket-SIPC
Summary:	IO::Socket::SIPC - Serialize Perl structures for inter process communication
Summary(pl.UTF-8):	IO::Socket::SIPC - serializacja struktur Perla do komunikacji międzyprocesowej
Name:		perl-IO-Socket-SIPC
Version:	0.07
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2650b8308dbc3ec1fb76734ac7ff01f6
URL:		http://search.cpan.org/dist/IO-Socket-SIPC/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(UNIVERSAL::require)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes it possible to transport Perl structures between
processes over sockets. It wraps your favorite IO::Socket module and
controls the amount of data over the socket. The default serializer is
Storable with nfreeze() and thaw() but you can choose each other
serializer you wish to use. You have just follow some restrictions and
need only some lines of code to adjust it for yourself. In addition
it's possible to use a checksum to check the integrity of the
transported data.

%description -l pl.UTF-8
Ten moduł umożliwia przesyłanie struktur Perla między procesami
poprzez gniazda. Obudowuje ulubiony moduł IO::Socket i kieruje dane
przez gniazdo. Domyślny serializer to Storable z nfreeze() i thaw(),
ale można wybrać dowolny inny. Wystarczy postępować zgodnie z pewnymi
restrykcjami i dopasować niewielką liczbę linii kodu. Ponadto istnieje
możliwość używania sumy kontrolnej do sprawdzania integralności
przesyłanych danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%{perl_vendorlib}/IO/Socket/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
