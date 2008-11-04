%define module   Exception-Class-TryCatch
%define version    1.12
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Syntactic tryE<sol>catch sugar for use with Exception::Class
Source:     http://www.cpan.org/modules/by-module/Exception/%{module}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{module}
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Exception::Class::TryCatch provides syntactic sugar for use with the
Exception::Class manpage using the familiar keywords 'try' and 'catch'. Its
primary objective is to allow users to avoid dealing directly with '$@' by
ensuring that any exceptions caught in an 'eval' are captured as the
Exception::Class manpage objects, whether they were thrown objects to begin
with or whether the error resulted from 'die'. This means that users may
immediately use 'isa' and various the Exception::Class manpage methods to
process the exception. 

In addition, this module provides for a method to push errors onto a hidden
error stack immediately after an 'eval' so that cleanup code or other error
handling may also call 'eval' without the original error in '$@' being
lost.

Inspiration for this module is due in part to Dave Rolsky's article
"Exception Handling in Perl With Exception::Class" in _The Perl Journal_
(Rolsky 2004).

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*

