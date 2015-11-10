%define  debug_package %{nil}

Summary:        Korora Extras
Name:           korora-extras
Version:        0.11
Release:        3%{?dist}.5
Source0:        %{name}-%{version}.tar.gz
License:        GPLv3+
Group:          System Environment/Base
Requires:       korora-release
BuildRequires:  policycoreutils libselinux
Obsoletes:      kororaa-extras
Provides:       kororaa-extras

%description
This package contains various files required for Korora
such as pretty bash shell, policykit overrides, vimrc, etc.

%prep
%setup -q

%build

%install
#mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
mkdir -p %{buildroot}%{_sysconfdir}/skel/Desktop
mkdir -p %{buildroot}%{_sysconfdir}/cron.hourly
mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
#mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_datadir}/polkit-1/rules.d
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/firefox/browser/defaults/profile

cp -a %{_builddir}/%{name}-%{version}/prefs.js %{buildroot}%{_libdir}/firefox/browser/defaults/profile/prefs.js

#cp -a %{_builddir}/%{name}-%{version}/*repo %{buildroot}%{_sysconfdir}/yum.repos.d/
install -m 0755 %{_builddir}/%{name}-%{version}/fstrim %{buildroot}%{_sysconfdir}/cron.hourly/fstrim
install -m 0755 %{_builddir}/%{name}-%{version}/vimrc %{buildroot}%{_sysconfdir}/skel/.vimrc
#cp -a %{_builddir}/%{name}-%{version}/01_korora %{buildroot}%{_sysconfdir}/sudoers.d/
install -m 0755 %{_builddir}/%{name}-%{version}/custom.sh %{buildroot}%{_sysconfdir}/profile.d/custom.sh
install -m 0644 %{_builddir}/%{name}-%{version}/dircolors.ansi-universal %{buildroot}%{_datadir}/%{name}/dircolors.ansi-universal
#install -m 0440 %{_builddir}/%{name}-%{version}/01_korora %{buildroot}%{_sysconfdir}/sudoers.d/01_korora
#cp -a %{_builddir}/%{name}-%{version}/*sh %{buildroot}%{_bindir}/
#removing this custom.sh because this goes under profile.d instead and I was lazy above and copied all shell scripts to bin
#rm %{buildroot}%{_bindir}/custom.sh
install -m 0644 %{_builddir}/%{name}-%{version}/10-korora-policy.rules %{buildroot}%{_datadir}/polkit-1/rules.d/10-korora-policy.rules
#cp -a %{_builddir}/%{name}-%{version}/adblockplus %{buildroot}/%{_libdir}/firefox/browser/defaults/profile/
#for x in Text.txt Image.png Presentation.odp Spreadsheet.ods Document.odt ; do touch %{buildroot}%{_sysconfdir}/skel/Templates/$x ; done
cp -a %{_builddir}/%{name}-%{version}/Templates %{buildroot}%{_sysconfdir}/skel/
/sbin/restorecon %{buildroot}%{_sharedstatedir}/polkit-1/localauthority/50-local.d/10-korora-overrides.pkla

#Set up system-wide hinting
ln -sf /usr/share/fontconfig/conf.avail/10-autohint.conf %{buildroot}/etc/fonts/conf.d/

%posttrans

%post
#Only do this on first install, not upgrades
#if [ "$1" == "1" ]
#then
  #Create vboxusers group
#  groupadd -r vboxusers 2>/dev/null

  #/sbin/restorecon '/var/lib/polkit-1/localauthority/50-local.d/10-korora-overrides.pkla'

  #Set installonly limit in yum.conf
#  if [ -z "$(grep installonly_limit=2 /etc/yum.conf)" ]
#  then
#    sed -i 's/^installonly_limit=.*/installonly_limit=2/g' /etc/yum.conf
#  fi

#  #Set clean_requirements_on_remove in yum.conf
#  if [ -z "$(grep clean_requirements_on_remove /etc/yum.conf)" ]
#  then
#    sed -i '/^installonly_limit=.*/ a clean_requirements_on_remove=1' /etc/yum.conf
#  else
#    sed -i 's/^clean_requirements_on_remove=.*/clean_requirements_on_remove=1/g' /etc/yum.conf
#  fi
#fi

%postun

%files
%defattr(-,root,root)
#%{_sysconfdir}/yum.repos.d/*repo
%{_sysconfdir}/cron.hourly/fstrim
%{_sysconfdir}/skel/.vimrc
%{_sysconfdir}/skel/Templates/*
#%{_sysconfdir}/sudoers.d/01_korora
%{_sysconfdir}/profile.d/custom.sh
%{_datadir}/%{name}/dircolors.ansi-universal
%{_datadir}/polkit-1/rules.d/10-korora-policy.rules
#%{_libdir}/firefox/browser/defaults/profile/adblockplus/
%{_sysconfdir}/fonts/conf.d/10-autohint.conf
%{_libdir}/firefox/browser/defaults/profile/prefs.js
#/etc/skel/Desktop/README.pdf

%changelog
* Thu Sep 24 2015 Chris Smart <csmart@kororaproject.org> 0.11-3
- Only run custom.sh if our shell is bash, else we brake zsh if there's no ~/.zshrc
- Update PS1 to use colour variables and reduce complexity checks for root.

* Mon Sep 7 2015 Chris Smart <csmart@kororaproject.org> 0.11-2
- Only show hostname on terminal PS1 when we are connected via SSH

* Thu Jul 23 2015 Chris Smart <csmart@kororaproject.org> 0.11-1
- Use solarized for color scheme to make it easier to see in major terminals

* Sun Jul 12 2015 Chris Smart <csmart@kororaproject.org> 0.10-2
- Use builtin git shell functions instead of custom bash script for PS1, thanks lithrem

* Sat Dec 20 2014 Chris Smart <csmart@kororaproject.org> 0.10-1
- Moved default firefox profile into common package from desktop specific ones.

* Sun Nov 16 2014 Ian Firns <firnsy@kororaproject.org> 0.9-1
- xterm does not support blength for disabling blink.

* Sat May 3 2014 Chris Smart <csmart@kororaproject.org> 0.8-3
- Fix setterm error when using non-interactive shell logins.
- Thanks to mdonnelly for fix.

* Tue Jan 28 2014 Chris Smart <csmart@kororaproject.org> 0.8-2
- Fix open document templates, empty files don't open.

* Sat Dec 28 2013 Chris Smart <csmart@kororaproject.org> 0.8-1
- Fix adblock plus subscription

* Thu Sep 25 2013 Chris Smart <csmart@kororaproject.org> 0.7-5
- Add cronjob for running fstrim

* Thu Sep 25 2013 Chris Smart <csmart@kororaproject.org> 0.7-4
- Fix font hinting link, which has moved to /usr/

* Sat Aug 17 2013 Chris Smart <csmart@kororaproject.org> 0.7-3
- Fix location of policykit overrides and format of file, which have changed.

* Sun Jun 16 2013 Chris Smart <csmart@kororaproject.org> 0.7-2
- Set clean_requirements_on_remove to yum.conf.

* Fri May 10 2013 Ian Firns <firnsy@kororaproject.org> 0.7-1
- Korora 19 release.

* Thu Oct 25 2012 Chris Smart <csmart@kororaproject.org> 0.6-2
- Korora 18 release.

* Mon May 14 2012 Chris Smart <chris@kororaa.org> 0.6-1
- Cleaned up for Kororaa 17 release, remove repo files (controlled by yum-repo), etc.

* Thu Nov 10 2011 Chris Smart <chris@kororaa.org> 0.5-1
- Clean up old Firefox profiles, enable system-wide antialiasing, Kororaa 16.

* Mon Oct 17 2011 Chris Smart <chris@kororaa.org> 0.4-8
- Fix akmod error on boot.

* Mon Oct 17 2011 Chris Smart <chris@kororaa.org> 0.4-7
- Fix google talk repo, arch by variable.

* Wed Oct 12 2011 Chris Smart <chris@kororaa.org> 0.4-6
- Remove cgroup from custom.sh, not needed anymore.

* Wed Oct 12 2011 Chris Smart <chris@kororaa.org> 0.4-5
- Fix firefox profile location.

* Tue Oct 11 2011 Chris Smart <chris@kororaa.org> 0.4-4
- Add repository for Google Talk Plugin.

* Wed Aug 31 2011 Chris Smart <chris@kororaa.org> 0.4-3
- Remove add-remove-extras dependency, replaced by jockey and flash-plugin-helper.

* Sun Aug 21 2011 Chris Smart <chris@kororaa.org> 0.4-2
- Updated for Firefox 6 and 7.

* Mon Jul 18 2011 Chris Smart <chris@kororaa.org> 0.4-1
- Fix lnk to README for Fedora 15, move links out of post into install.

* Tue Jul 11 2011 Chris Smart <chris@kororaa.org> 0.3-3
- Remove cgroups for fedora 15.

* Fri Jul 08 2011 Chris Smart <chris@kororaa.org> 0.3-2
- Support for Firefox 5 (default profile), remove cgroups for fedora 15.

* Tue Apr 26 2011 Chris Smart <chris@kororaa.org> 0.3-2
- Remove the cgroup cleanup from postun, as this runs on package upgrades and breaks system.

* Wed Apr 06 2011 Chris Smart <chris@kororaa.org> 0.3-1
- Added cgroup to kororaa-extras, added GNOME tweaks.

* Tue Mar 29 2011 Chris Smart <chris@kororaa.org> 0.2-4.2
- Added cgroup to kororaa-extras, added GNOME tweaks.

* Sun Mar 23 2011 Chris Smart <chris@kororaa.org> 0.2-4
- Added Firefox user.js, added profile.d/custom.sh for bash tweaks, vimrc and Desktop links to skel, changes to config files.

* Sun Mar 23 2011 Chris Smart <chris@kororaa.org> 0.1-4
- Added Firefox4 repo, fix incorrect permissions on sudoers file.

* Sun Feb 27 2011 Chris Smart <chris@kororaa.org> 0.1-1
- Initial port.

