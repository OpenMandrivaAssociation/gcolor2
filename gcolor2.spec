Name:		gcolor2
Version:	0.4
Release:	%mkrel 1
Summary:	Simple color selector
Group:		Graphics
License:	GPL
URL:		http://gcolor2.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/gcolor2/%{name}-%{version}.tar.bz2       
Patch1:		gcolor2-french.patch.bz2

BuildRequires:	gtk2-devel
BuildRequires:	ImageMagick perl(XML::Parser)

%description 
Gcolor2 is a GTK2 color selector to provide a quick and easy way to find
colors for whatever task is at hand. Colors can be saved and deleted as well.

%prep
%setup -q
%patch1 -p1 -b .french

%build
alias libtoolize=true
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%{find_lang} %{name}

# Menu
mkdir -p %{buildroot}%{_menudir}
cat >%{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/%{name}" needs="X11" \
icon="%{name}.png" section="Multimedia/Graphics" \
title="GColor2" longtitle="GTK2 color chooser"
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/icon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/icon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/icon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%post
%{update_menus}

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_menudir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
