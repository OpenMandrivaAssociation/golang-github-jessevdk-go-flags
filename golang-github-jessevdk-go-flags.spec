# http://github.com/jessevdk/go-flags
%global goipath         github.com/jessevdk/go-flags
%global import_path     %{goipath}
%global commit          97448c91aac742cbca3d020b3e769013a420a06f

%gometa -i

Name:           golang-github-jessevdk-go-flags
Version:        0
Release:        0.14%{?dist}
Summary:        Go command line option parser
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup

%install
%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Marek Skalický <mskalick@redhat.com> - 0-0.13.20160207git97448c9
- Rebase to version used by mongo-tools 3.6

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20160626gitf2785f5
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitf2785f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitf2785f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitf2785f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitf2785f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 25 2016 jchaloup <jchaloup@redhat.com> - 0-0.7.gitf2785f5
- Bump to upstream f2785f5820ec967043de79c8be97edfc464ca745
  related: #1250487

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git5e11878
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git5e11878
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git5e11878
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git5e11878
- Update to spec-2.1
  related: #1250487

* Thu Aug 06 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git5e11878
- Update spec file to spec-2.0
  resolves: #1250487

* Mon Jun 15 2015 Marek Skalicky <mskalick@redhat.com> - 0-0.1.git5e11878
- First package for Fedora
  resolves: #1232218

