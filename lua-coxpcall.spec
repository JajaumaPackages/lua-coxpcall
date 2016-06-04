%global debug_package %{nil}

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
# for arch-independent modules
%global luapkgdir %{_datadir}/lua/%{luaver}

%define vermagic1 1
%define vermagic2 16
%define vermagic3 0

Name:           lua-coxpcall
Version:        %{vermagic1}.%{vermagic2}.%{vermagic3}
Release:        1%{?dist}
Summary:        Coroutine safe xpcall and pcall

License:        MIT
URL:            http://keplerproject.github.io/coxpcall/
Source0:        https://github.com/keplerproject/coxpcall/archive/v%{vermagic1}_%{vermagic2}_%{vermagic3}.tar.gz

BuildArch:      noarch
BuildRequires:  lua-devel >= %{luaver}
%if 0%{?rhel} == 6
Requires:       lua >= %{luaver}
Requires:       lua < 5.2
%else
Requires:       lua(abi) >= %{luaver}
%endif

%description
Coxpcall encapsulates the protected calls with a coroutine based loop, so
errors can be dealed without the usual pcall/xpcall issues with coroutines.


%prep
%setup -q -n coxpcall-%{vermagic1}_%{vermagic2}_%{vermagic3}


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{luapkgdir}
make install LUA_DIR=%{buildroot}%{luapkgdir}


%files
%doc README.md doc/
%{luapkgdir}/*


%changelog
* Sat Jun 04 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.16.0-1
- Public release
