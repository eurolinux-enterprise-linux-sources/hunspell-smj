Name: hunspell-smj
Summary: Lule Saami hunspell dictionaries
Version: 1.0
Release: 0.7.beta7%{?dist}
Source: http://divvun.no/static_files/hunspell-smj.tar.gz
Group: Applications/Text
URL: http://www.divvun.no/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3
BuildArch: noarch

Requires: hunspell

%description
Lule Saami hunspell dictionaries.

%prep
%setup -q -n %{name}-1.0beta7.20090316

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p smj.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/smj_NO.aff
cp -p smj.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/smj_NO.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
smj_NO_aliases="smj_SE"
for lang in $smj_NO_aliases; do
        ln -s smj_NO.aff $lang.aff
        ln -s smj_NO.dic $lang.dic
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Copyright README GPL-3
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-0.7.beta7
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Caolan McNamara <caolanm@redhat.com> - 1.0-0.1.beta7
- initial version
