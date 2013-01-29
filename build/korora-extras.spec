Summary:        Korora Extras
Name:           korora-extras
Version:        0.6
Release:        2%{?dist}.1
Source0:        %{name}-%{version}.tar.gz
License:        GPLv3+
Group:          System Environment/Base
Requires:       korora-release sed coreutils akmods yum git vim fontconfig
BuildRequires:  policycoreutils libselinux
Obsoletes:      kororaa-extras
Provides:       kororaa-extras

%description
This package contains various files required for Kororaa
such as pretty bash shell, policykit overrides, vimrc, etc.

%prep
%setup -q

%build

%install
#mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
mkdir -p %{buildroot}%{_sysconfdir}/skel/Desktop
mkdir -p %{buildroot}%{_sysconfdir}/skel/Templates
mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
#mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_sharedstatedir}/polkit-1/localauthority/50-local.d/
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/firefox/defaults/profile

#cp -a %{_builddir}/%{name}-%{version}/*repo %{buildroot}%{_sysconfdir}/yum.repos.d/
install -m 0755 %{_builddir}/%{name}-%{version}/vimrc %{buildroot}%{_sysconfdir}/skel/.vimrc
#cp -a %{_builddir}/%{name}-%{version}/01_korora %{buildroot}%{_sysconfdir}/sudoers.d/
install -m 0755 %{_builddir}/%{name}-%{version}/custom.sh %{buildroot}%{_sysconfdir}/profile.d/custom.sh
install -m 0755 %{_builddir}/%{name}-%{version}/parse-git-branch.sh %{buildroot}%{_bindir}/parse-git-branch.sh
#install -m 0440 %{_builddir}/%{name}-%{version}/01_korora %{buildroot}%{_sysconfdir}/sudoers.d/01_korora
#cp -a %{_builddir}/%{name}-%{version}/*sh %{buildroot}%{_bindir}/
#removing this custom.sh because this goes under profile.d instead and I was lazy above and copied all shell scripts to bin
#rm %{buildroot}%{_bindir}/custom.sh
install -m 0644 %{_builddir}/%{name}-%{version}/10-korora-overrides.pkla %{buildroot}%{_sharedstatedir}/polkit-1/localauthority/50-local.d/
cp -a %{_builddir}/%{name}-%{version}/adblockplus %{buildroot}/%{_libdir}/firefox/defaults/profile/
for x in Drawing.odg Presentation.odp Spreadsheet.ods Document.odt ; do touch %{buildroot}%{_sysconfdir}/skel/Templates/$x ; done
/sbin/restorecon %{buildroot}%{_sharedstatedir}/polkit-1/localauthority/50-local.d/10-korora-overrides.pkla

#links
cd %{buildroot}/
ln -sf /usr/share/doc/korora-release-18/README.pdf %{buildroot}/etc/skel/Desktop/README.pdf
cd -

#Set up system-wide hinting
ln -sf /etc/fonts/conf.avail/10-autohint.conf %{buildroot}/etc/fonts/conf.d/

#Others
#chmod a+x %{buildroot}%{_bindir}/parse-git-branch.sh

%posttrans

%post
#Create vboxusers group
groupadd -r vboxusers 2>/dev/null

#/sbin/restorecon '/var/lib/polkit-1/localauthority/50-local.d/10-korora-overrides.pkla'

#Set installonly limit in yum.conf
if [ -z "$(grep installonly_limit=2 /etc/yum.conf)" ]
then
  sed -i 's/^installonly_limit=.*/installonly_limit=2/g' /etc/yum.conf
fi

#Not needed now because we are using our own adobe-release package
##Disable AdobeReader, if using adobe repo
#if [ -e /etc/yum.repos.d/adobe-linux-i386.repo -a -z "$(grep exclude=AdobeReader* /etc/yum.repos.d/adobe-linux-i386.repo 2>/dev/null)" ]
#then
#  echo "exclude=AdobeReader*" >> /etc/yum.repos.d/adobe-linux-i386.repo
#fi
##We might be on 64bit with 64bit adobe, or we might be on 64bit with 32bit adobe.., so best check
#if [ -e /etc/yum.repos.d/adobe-linux-x86_64.repo -a -z "$(grep exclude=AdobeReader* /etc/yum.repos.d/adobe-linux-x86_64.repo 2>/dev/null)" ]
#then
#  echo "exclude=AdobeReader*" >> /etc/yum.repos.d/adobe-linux-x86_64.repo
#fi

#Fix error on akmods boot
#if [ -n "$(grep "exit \${1:-128}" /usr/sbin/akmods)" ]
#then
#  sed -i s/exit\ \${1:-128}/exit\ \${1:0}/ /usr/sbin/akmods
#fi

#cleanup obsolete firefox profile locations
#rm -Rf %{_libdir}/firefox-{3.6,4,5,6,7,8} 2>/dev/null

#%ifarch x86_64
#if [ -f /etc/yum.repos.d/adobe-linux-i386.repo ]
#then
#  sed -i s/i386/x86_64/ /etc/yum.repos.d/adobe-linux-i386.repo
#  mv /etc/yum.repos.d/adobe-linux-i386.repo /etc/yum.repos.d/adobe-linux-x86_64.repo
#fi
#%endif

%postun

%files
%defattr(-,root,root)
#%{_sysconfdir}/yum.repos.d/*repo
%{_sysconfdir}/skel/.vimrc
%{_sysconfdir}/skel/Templates/*
#%{_sysconfdir}/sudoers.d/01_korora
%{_sysconfdir}/profile.d/custom.sh
%{_bindir}/*sh
%{_sharedstatedir}/polkit-1/localauthority/50-local.d/*pkla
%{_libdir}/firefox/defaults/profile/adblockplus/
/etc/skel/Desktop/README.pdf
/etc/fonts/conf.d/10-autohint.conf

%changelog
* Thu Oct 25 2012 Chris Smart <csmart@kororaproject.org> 0.6-2
- Kororaa 18 release.

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

