# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       endless-sky

# >> macros
# << macros
%define dataversion 0.10.2
%define finaldatadir /home/.local/share/%{name}

Summary:    Space exploration, trading, and combat game
Version:    0.10.2
Release:    0
Group:      Applications
License:    GPLv3+
URL:        https://endless-sky.github.io/
Source0:    %{name}-%{version}.tar.gz
Source1:    %{name}.desktop
Source2:    %{name}.profile
Source100:  endless-sky.yaml
Source101:  endless-sky-rpmlintrc
Patch0:     %{name}-cmake319.patch
Patch1:     %{name}-cmake-no-glew.patch
Patch2:     %{name}-cmake-gles23.patch
Patch3:     %{name}-install-destination.patch
Patch4:     b5e0225ea60c00695c59d8caa8a7a4d48b7bc90c.diff
Requires:   %{name}-gamedata-meta  = %{dataversion}
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  cmake >= 3.19.0, cmake < 3.26.0
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  ninja
BuildRequires:  fdupes
BuildRequires:  desktop-file-utils

%description
Endless Sky is a 2D space trading and combat game similar to the classic
Escape Velocity series.

Explore other star systems.  Earn money by trading, carrying passengers, or
completing missions. Use your earnings to buy a better ship or to upgrade
the weapons and engines on your current one.

Blow up pirates. Take sides in a civil war. Or leave human space behind and
hope to find friendly aliens whose culture is more civilized than your own.

NOTE: To run this, you need to either install the -data meta-package, or
      provide the game data youself. It is expected to be in /home/.system/usr/share/endless-sky/data

%if "%{?vendor}" == "chum"
PackageName: Endless Sky
Type: desktop-application
DeveloperName: Michael Zahniser
PackagedBy: nephros
Categories:
  - Games
Custom:
  Repo: https://github.com/endless-sky/endless-sky
  PackagingRepo: https://github.com/nephros/endless-sky
Icon: https://github.com/endless-sky/endless-sky/blob/master/icons/icon_128x128.png?raw=true
Url:
  Homepage: %{url}
%endif


%package data
Summary:    Gamedata Meta package for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-gamedata-meta-sounds  = %{dataversion}
Requires:   %{name}-gamedata-meta-images1 = %{dataversion}
Requires:   %{name}-gamedata-meta-images2 = %{dataversion}
Requires:   %{name}-gamedata-meta-images3 = %{dataversion}
Requires:   %{name}-gamedata-meta-images4 = %{dataversion}
Requires:   %{name}-gamedata-meta-images5 = %{dataversion}
Provides:   %{name}-gamedata-meta  = %{dataversion}

%description data
%{summary}.

%package data-images1
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-gamedata-meta-images1  = %{dataversion}

%description data-images1
%{summary}.

%package data-images2
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-gamedata-meta-images2  = %{dataversion}

%description data-images2
%{summary}.

%package data-images3
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-gamedata-meta-images3  = %{dataversion}

%description data-images3
%{summary}.

%package data-images4
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-gamedata-meta-images4  = %{dataversion}

%description data-images4
%{summary}.

%package data-images5
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-gamedata-meta-images5  = %{dataversion}

%description data-images5
%{summary}.

%package data-sounds
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-gamedata-meta-sounds  = %{dataversion}

%description data-sounds
%{summary}.

%prep
%setup -q -n %{name}-%{version}/upstream

# %{name}-cmake319.patch
%patch0 -p1
# %{name}-cmake-no-glew.patch
%patch1 -p1
# %{name}-cmake-gles23.patch
%patch2 -p1
# %{name}-install-destination.patch
%patch3 -p1
# b5e0225ea60c00695c59d8caa8a7a4d48b7bc90c.diff
%patch4 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -G Ninja \
    -DSAILFISHOS=ON \
    -DCMAKE_RULE_MESSAGES=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_COLOR_DIAGNOSTICS=OFF \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
    -DCMAKE_RULE_MESSAGES=ON \
    -DBUILD_TESTING=OFF \
    -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
    -DES_USE_VCPKG=OFF \
    -DES_GLES=ON \
    -DES_USE_SYSTEM_LIBRARIES=ON \
    -DES_CREATE_BUNDLE=OFF \
    -DPKG_CONFIG_USE_CMAKE_PREFIX_PATH=ON


# >> build post
%ninja_build
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%__install -d -m 0755 "%{buildroot}%{_datadir}/%{name}"
%__install -D -m 0644  %{SOURCE1} %{buildroot}%{_datadir}/applications
%__install -D -m 0644  %{SOURCE2} %{buildroot}%{_sysconfdir}/sailjail/permissions

%ninja_install
# << install pre

# >> install post
%fdupes %{buildroot}%{_datadir}/%{name}/images
# move resource data to /home/.system
%__install -d -m 0755 "%{buildroot}%{finaldatadir}"
mv %{buildroot}%{_datadir}/%{name}/images %{buildroot}%{finaldatadir}/
mv %{buildroot}%{_datadir}/%{name}/data %{buildroot}%{finaldatadir}/
mv %{buildroot}%{_datadir}/%{name}/sounds %{buildroot}%{finaldatadir}/
mv %{buildroot}%{_datadir}/%{name}/credits.txt %{buildroot}%{finaldatadir}/
mv %{buildroot}%{_datadir}/%{name}/keys.txt %{buildroot}%{finaldatadir}/
ln -s %{finaldatadir} %{buildroot}%{_datadir}/%{name}/resources
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%license license.txt
%license copyright
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/endless-sky.png
%dir %{finaldatadir}
%config %{_sysconfdir}/sailjail/permissions/%{name}.profile
%exclude %{_datadir}/doc/endless-sky/*
%exclude %{_datadir}/man/man6/endless-sky.6.gz
%exclude %{_datadir}/metainfo/io.github.endless_sky.endless_sky.appdata.xml
# >> files
# << files

%files data
%defattr(-,root,root,-)
%license copyright
%{_datadir}/%{name}/resources
%{finaldatadir}/data
%{finaldatadir}/credits.txt
%{finaldatadir}/keys.txt
%dir %{finaldatadir}/images
# >> files data
# << files data

%files data-images1
%defattr(-,root,root,-)
%{finaldatadir}/images/_menu
%{finaldatadir}/images/asteroid
%{finaldatadir}/images/effect
%{finaldatadir}/images/font
# >> files data-images1
# << files data-images1

%files data-images2
%defattr(-,root,root,-)
%{finaldatadir}/images/hardpoint
%{finaldatadir}/images/icon
%{finaldatadir}/images/label
%{finaldatadir}/images/land
# >> files data-images2
# << files data-images2

%files data-images3
%defattr(-,root,root,-)
%{finaldatadir}/images/outfit
%{finaldatadir}/images/planet
%{finaldatadir}/images/portrait
%{finaldatadir}/images/projectile
# >> files data-images3
# << files data-images3

%files data-images4
%defattr(-,root,root,-)
%{finaldatadir}/images/scene
%{finaldatadir}/images/ship
%{finaldatadir}/images/star
# >> files data-images4
# << files data-images4

%files data-images5
%defattr(-,root,root,-)
%{finaldatadir}/images/thumbnail
%{finaldatadir}/images/ui
# >> files data-images5
# << files data-images5

%files data-sounds
%defattr(-,root,root,-)
%{finaldatadir}/sounds
# >> files data-sounds
# << files data-sounds
