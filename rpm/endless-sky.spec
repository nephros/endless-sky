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
Group:      Applications
Requires:   %{name} = %{version}-%{release}

%description data
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
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_bindir}/endless-sky
%{_datadir}/icons/hicolor/*/apps/endless-sky.png
%exclude %{_datadir}/doc/endless-sky/*
%exclude %{_datadir}/man/man6/endless-sky.6.gz
%exclude %{_datadir}/metainfo/io.github.endless_sky.endless_sky.appdata.xml
# >> files
# << files

%files data
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/*
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/*
%dir %{_datadir}/%{name}/sounds
%{_datadir}/%{name}/sounds/*
# >> files data
# << files data
