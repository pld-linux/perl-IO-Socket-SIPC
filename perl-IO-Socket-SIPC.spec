#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Socket-SIPC
Summary:	IO::Socket::SIPC - Serialize perl structures for inter process communication.
#Summary(pl):	
Name:		perl-IO-Socket-SIPC
Version:	0.04
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	99623d1913defe8f58e4ec0ee934fe88
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(UNIVERSAL::require)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes it possible to transport perl structures between processes over sockets.
It wrappes your favorite IO::Socket module and controls the amount of data over the socket.
The default serializer is Storable with nfreeze() and thaw() but you can choose each
other serializer you wish to use. You have just follow some restrictions and need only some
lines of code to adjust it for yourself. In addition it's possible to use a checksum to check
the integrity of the transported data. Take a look to the method section.



# %description -l pl
# TODO

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
#%%{perl_vendorlib}/IO/Socket/SIPC
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
