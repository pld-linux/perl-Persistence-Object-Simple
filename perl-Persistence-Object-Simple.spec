#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Persistence
%define	pnam	Object-Persistence
Summary:	Persistence::Object::Simple - object persistence with Data::Dumper
Summary(pl):	Persistence::Object::Simple - trwa�e obiekty z u�yciem Data::Dumper
Name:		perl-Persistence-Object-Simple
Version:	0.92
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	72638cb6931360ce65fb653e9b6ef6b0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Persistence::Object::Simple provides persistence functionality to its
objects. Object definitions are stored as stringified Perl data
structures, generated with Data::Dumper, that are amenable to manual
editing and external processing from outside the class interface.

%description -l pl
Persistence::Object::Simple daje funkcjonalno�� przechowywania dla
swoich obiekt�w. Definicje obiekt�w s� przechowywane jako
przekszta�cone na �a�cuchy struktury danych Perla, wygenerowane przy
pomocy modu�u Data::Dumper, b�d�ce odpowiedzialnymi za r�czn� edycj�
i zewn�trzne przetwarzanie na zewn�trz interfejsu klas.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Persistence
%{perl_vendorlib}/Persistence/Database.pm
%{perl_vendorlib}/Persistence/Object
%{_mandir}/man3/*
