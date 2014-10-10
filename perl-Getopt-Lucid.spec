%define upstream_name    Getopt-Lucid
%define upstream_version 1.05
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.05
Release:	2

Summary:	Clear, readable syntax for command line processing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Getopt/Getopt-Lucid-1.05.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(Exception::Class::TryCatch)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
The goal of this module is providing good code readability and clarity of
intent for command-line option processing. While readability is a
subjective standard, Getopt::Lucid relies on a more verbose, plain-English
option specification as compared against the more symbolic approach of
Getopt::Long. Key features include:

  Five option types: switches, counters, parameters, lists, and keypairs

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.190.0-2mdv2011.0
+ Revision: 656921
- rebuild for updated spec-helper

* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 596525
- update to new version 0.19

* Thu Nov 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 467461
- import perl-Getopt-Lucid


* Thu Nov 19 2009 cpan2dist 0.18-1mdv
- initial mdv release, generated with cpan2dist

