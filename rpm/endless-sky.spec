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
License:    GPLv3
URL:        https://endless-sky.github.io/
Source0:    %{name}-%{version}.tar.gz
Source100:  endless-sky.yaml
Source101:  endless-sky-rpmlintrc
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  cmake >= 3.21.0
BuildRequires:  gcc-c++
BuildRequires:  SDL2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  OpenAL-devel
BuildRequires:  desktop-file-utils

%description
${summary}.

%if "%{?vendor}" == "chum"
PackageName: Endless Sky
Type: desktop-application
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


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DES_USE_VCPKG=OFF \
    -DES_GLES=ON \
    -DES_USE_SYSTEM_LIBRARIES=ON \
    -DES_USE_OFFSCREEN=OFF \
    -DES_CREATE_BUNDLE=OFF

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# mangle version info
sed -i -e "s/unreleased/%{version}/" %{buildroot}%{_datadir}/%{name}/qml/%{name}.qml
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%license LICENSE
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
# >> files
# << files
