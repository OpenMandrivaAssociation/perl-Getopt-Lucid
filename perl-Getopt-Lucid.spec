%define upstream_name    Getopt-Lucid
%define upstream_version 0.19

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Clear, readable syntax for command line processing
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Getopt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Exception::Class::TryCatch)
BuildRequires: perl(Exporter)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The goal of this module is providing good code readability and clarity of
intent for command-line option processing. While readability is a
subjective standard, Getopt::Lucid relies on a more verbose, plain-English
option specification as compared against the more symbolic approach of
Getopt::Long. Key features include:

* *

  Five option types: switches, counters, parameters, lists, and keypairs

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


