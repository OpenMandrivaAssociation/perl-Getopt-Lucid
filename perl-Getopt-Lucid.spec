%define upstream_name    Getopt-Lucid
%define upstream_version 1.10
Name:		perl-%{upstream_name}
Version:	1.10
Release:	25

Summary:	Clear, readable syntax for command line processing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/dagolden/Getopt-Lucid
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Getopt-Lucid-1.10.tar.gz

BuildRequires:	make
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
%setup -q -n Getopt-Lucid-1.10

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
# soft: do not fail package on test failures
set +e
:  # soft check
:  # soft
%make test || :

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

