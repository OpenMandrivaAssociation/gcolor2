Name:		gcolor2
Version:	0.4
Release:	%mkrel 6
Summary:	Simple color selector
Group:		Graphics
License:	GPL
URL:		http://gcolor2.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/gcolor2/%{name}-%{version}.tar.bz2       
Patch0:		gcolor2-french.patch.bz2
Patch1:		gcolor2-0.4-amd64.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}

BuildRequires:	gtk2-devel
BuildRequires:	imagemagick perl(XML::Parser)

%description 
Gcolor2 is a GTK2 color selector to provide a quick and easy way to find
colors for whatever task is at hand. Colors can be saved and deleted as well.

%prep
%setup -q
%patch0 -p1 -b .french
%patch1 -p1

%build
alias libtoolize=true
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%{find_lang} %{name}

# Menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application 
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=GNOME;GTK;Graphics;Viewer
Name=GColor2
Comment=GTK2 color chooser
EOF

#icons
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 pixmaps/icon.png %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 pixmaps/icon.png %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 pixmaps/icon.png %{buildroot}/%_miconsdir/%name.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png

