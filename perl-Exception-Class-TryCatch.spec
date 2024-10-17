%define upstream_name    Exception-Class-TryCatch%define upstream_version 1.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Syntactic tryE<sol>catch sugar for use with Exception::Class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Exception/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.120.0-2mdv2011.0
+ Revision: 654185
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 405857
- rebuild using %%perl_convert_version

* Tue Nov 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2009.1
+ Revision: 299759
- update to new version 1.12

* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2009.1
+ Revision: 291361
- import perl-Exception-Class-TryCatch


* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2009.1
- initial mdv release, generated with cpan2dist


