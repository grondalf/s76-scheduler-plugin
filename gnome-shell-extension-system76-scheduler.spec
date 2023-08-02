%global uuid s76-scheduler@mattjakeman.com

Name:        gnome-shell-extension-system76-scheduler
Version:     {{{ git_dir_version }}}
Release:     1%{?dist}
Summary:	 Standalone GNOME Shell integration for system76-scheduler to make the desktop more responsive.

Group:       User Interface/Desktops
License:     GPLv3
URL:         https://github.com/KyleGospo/s76-scheduler-plugin
Source0:     https://github.com/KyleGospo/s76-scheduler-plugin/archive/refs/heads/master.tar.gz
BuildArch:   noarch

Requires:    gnome-shell >= 3.12
Requires:    system76-scheduler
%description
This is a standalone extension that integrates system76-scheduler without needing pop-shell installed. The majority of code in this plugin comes from pop-shell and is used under the GPL-3.0 licence.

%prep
%autosetup -n s76-scheduler-plugin-master

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}