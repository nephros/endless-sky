# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       endless-sky

# >> macros
# << macros
%define orgname org.nephros.sailfish
%define appname AppTemplate
%define pkgname %{name}
%define servicebase %{orgname}.%{appname}

Summary:    Space exploration, trading, and combat game.
Version:    0.10.2
Release:    0
Group:      Applications
License:    GPLv3+
URL:        https://endless-sky.github.io/
Source0:    %{name}-%{version}.tar.gz
Source100:  endless-sky.yaml
Source101:  endless-sky-rpmlintrc
Patch0:     %{name}-install-destination.patch
Requires:   %{name}-data
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  cmake >= 3.21.0
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  ninja
BuildRequires:  SDL2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  OpenAL-devel
BuildRequires:  desktop-file-utils

%description
Endless Sky is a 2D space trading and combat game similar to the classic
Escape Velocity series. Explore other star systems.

Earn money by trading, carrying passengers, or completing missions. Use
your earnings to buy a better ship or to upgrade the weapons and engines on
your current one.

Blow up pirates. Take sides in a civil war. Or leave human space behind and
hope to find friendly aliens whose culture is more civilized than your own.

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
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-data-sounds
Requires:   %{name}-data-images1
Requires:   %{name}-data-images2
Requires:   %{name}-data-images3
Requires:   %{name}-data-images4

%description data
%{summary}.

%package data-images1
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description data-images1
%{summary}.

%package data-images2
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description data-images2
%{summary}.

%package data-images3
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description data-images3
%{summary}.

%package data-images4
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description data-images4
%{summary}.

%package data-sounds
Summary:    Gamedata for %{name}
License:    GPLv2 and CC0 and CC-BY-SA-4.0 and CC-BY-SA-2.0 and CC-BY-SA-3.0 and public-domain
Group:      Applications
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description data-sounds
%{summary}.

%prep
%setup -q -n %{name}-%{version}/upstream

# %{name}-install-destination.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# Fix glew to not use GLU:
export GLEW_NO_GLU=-DGLEW_NO_GLU
export CFLAGS="$CFLAGS -DGLEW_NO_GLU"
export CXXFLAGS="$CXXFLAGS -DGLEW_NO_GLU"
# << build pre

%cmake .  \
    -DCMAKE_RULE_MESSAGES:BOOL=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING=OFF \
    -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
    -DES_USE_VCPKG=OFF \
    -DES_GLES=ON \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DES_USE_SYSTEM_LIBRARIES=ON \
    -DES_CREATE_BUNDLE=OFF \
    -DPKG_CONFIG_USE_CMAKE_PREFIX_PATH=ON \
    -DCMAKE_PREFIX_PATH="%{_libdir}/glvnd;%{_libdir}/pkgconfig/glvnd;" \
    -DCMAKE_INCLUDE_PATH="%{_includedir}/glvnd" \
    -DGLEW_NO_GLU:BOOL=ON \
    -DCMAKE_C_CFLAGS="${CMAKE_C_CFLAGS} -DGLEW_NO_GLU" \
    -DCMAKE_CXX_CFLAGS="${CMAKE_CXX_CFLAGS} -DGLEW_NO_GLU"

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%__install -d -m 0755 "%{buildroot}%{_datadir}/%{name}"

# << install pre
%make_install

# >> install post
# Fix invlaid entries:
sed -i -e '/^Version.*$/d;/^SingleMainWindow/d' %{buildroot}%{_datadir}/applications/*.desktop
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%license copyright
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/credits.txt
%{_datadir}/%{name}/keys.txt
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/endless-sky.png
%exclude %{_datadir}/doc/endless-sky/*
%exclude %{_datadir}/man/man6/endless-sky.6.gz
%exclude %{_datadir}/metainfo/io.github.endless_sky.endless_sky.appdata.xml
# >> files
# << files

%files data
%defattr(-,root,root,-)
%license copyright
%{_datadir}/%{name}/data
%dir %{_datadir}/%{name}/images
# >> files data
# << files data

%files data-images1
%defattr(-,root,root,-)
%{_datadir}/%{name}/images/_menu
%{_datadir}/%{name}/images/asteroid
%{_datadir}/%{name}/images/effect
%{_datadir}/%{name}/images/font
# >> files data-images1
# << files data-images1

%files data-images2
%defattr(-,root,root,-)
%{_datadir}/%{name}/images/hardpoint
%{_datadir}/%{name}/images/icon
%{_datadir}/%{name}/images/label
%{_datadir}/%{name}/images/land
# >> files data-images2
# << files data-images2

%files data-images3
%defattr(-,root,root,-)
%{_datadir}/%{name}/images/outfit
%{_datadir}/%{name}/images/planet
%{_datadir}/%{name}/images/portrait
%{_datadir}/%{name}/images/projectile
# >> files data-images3
# << files data-images3

%files data-images4
%defattr(-,root,root,-)
%{_datadir}/%{name}/images/scene
%{_datadir}/%{name}/images/ship
%{_datadir}/%{name}/images/star
%{_datadir}/%{name}/images/thumbnail
%{_datadir}/%{name}/images/ui
# >> files data-images4
# << files data-images4

%files data-sounds
%defattr(-,root,root,-)
%{_datadir}/%{name}/sounds
# >> files data-sounds
# << files data-sounds
