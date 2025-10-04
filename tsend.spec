
%if 0%{?bash_completions_dir:1} == 0
%global bash_completions_dir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo "/etc/bash_completion.d")
%endif

Name:		tsend
Version:	0.4.0
Release:	1%{?dist}
Summary:	Sending telegram messages from command line

License:	Freely redistributable without restriction
URL:		http://mediawiki.nita.ru/tsend
Source0:	http://gitserver/DevOps/scripts/tsend/snapshot/%{name}-%{version}.tar.bz2

BuildArch:	noarch

BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	cmake

Requires:	bash
Requires:	jq
Requires:	curl

%description
Sending telegram messages from command line.

%{?__cmake_in_source_build:%global	__cmake_in_source_build	%{nil}}
%{!?_vpath_builddir:%global _vpath_builddir %{_vendor}-%{_target_os}-build}

%prep
:

%build
%cmake

%install
rm -rf %{buildroot}
%cmake_install


%files
%defattr(-,root,root,-)
%{_bindir}/tsend
%{bash_completions_dir}/tsend


%changelog
* Sat Oct  4 2025 Богаченков Вячеслав <bvy@nita.ru> - 0.4.0-1
- проект переведён на cmake

* Fri Jul  4 2025 Богаченков Вячеслав <bvy@nita.ru> - 0.3.1-1
- Дополнен вывод справки
- Раскрашен вывод справки (#32529)
- Испарвлен вывод версии (#32528)

* Fri Jun 20 2025 Богаченков Вячеслав <bvy@nita.ru> - 0.3.0-1
- переход на сборку rpm из проекта (#32436)

* Thu Dec 05 2024 Богаченков Вячеслав <bvy@nita.ru> - 0.1.1-1
- инициализация (#23002)
