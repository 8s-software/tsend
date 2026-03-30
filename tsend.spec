
%if 0%{?bash_completions_dir:1} == 0
%global bash_completions_dir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo "/etc/bash_completion.d")
%endif

Name:		tsend
Version:	0.5.0
Release:	1%{?dist}
Summary:	Sending telegram messages from command line
Group:		Applications/Communications

License:	Freely redistributable without restriction
URL:		http://mediawiki.nita.ru/tsend
Source0:	http://gitserver/DevOps/scripts/tsend/snapshot/%{name}-%{version}.tar.bz2

BuildArch:	noarch

BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	cmake
BuildRequires:	cmake-rpm-macros

Requires:	bash
Requires:	jq
Requires:	curl
Requires:	bash-completion
Requires:	util-linux
Requires:	coreutils
Requires:	c2e

%description
Sending telegram messages from command line.

%{?__cmake_in_source_build:%global __cmake_in_source_build %{nil}}
%{!?_vpath_builddir:%global _vpath_builddir %{_vendor}-%{_target_os}-build}
%{!?_vpath_srcdir:%global _vpath_srcdir .}

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
* Mon Mar 30 2026 Богаченков Вячеслав <bvy@nita.ru> - 0.5.0-1
- добавлена поддержка отправки сообщений через SOCKS5 прокси (#34383)

* Wed Feb 25 2026 Богаченков Вячеслав <bvy@nita.ru> - 0.4.4-1
- добавлена зависимость от c2e (#34186)

* Wed Feb 25 2026 Богаченков Вячеслав <bvy@nita.ru> - 0.4.3-1
- поправлена цветовая схема справки и отформатирован текст (#34184) (#34185)

* Thu Oct 23 2025 Богаченков Вячеслав <bvy@nita.ru> - 0.4.2-1
- добавлены недостающие зависимости (#33384)

* Wed Oct 22 2025 Богаченков Вячеслав <bvy@nita.ru> - 0.4.1-1
- исправлено отображение версии (#33365)

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
