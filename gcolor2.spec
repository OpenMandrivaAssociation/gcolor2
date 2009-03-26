Name:		gcolor2
Version:	0.4
Release:	%mkrel 17
Summary:	Simple color selector
Group:		Graphics
License:	GPLv2+
URL:		http://gcolor2.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/gcolor2/%{name}-%{version}.tar.bz2
Source1:	gcolor2-pofiles.tar.bz2

Patch1:		gcolor2-0.4-amd64.patch
Patch2:		gcolor2-i18n.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}

BuildRequires:	gtk2-devel
BuildRequires:	imagemagick perl(XML::Parser)
BuildRequires:	intltool

%description 
Gcolor2 is a GTK2 color selector to provide a quick and easy way to find
colors for whatever task is at hand. Colors can be saved and deleted as well.

%prep
%setup -q -a1
%patch1 -p1
%patch2 -p1

%build
echo "gcolor2.glade" >> po/POTFILES.in

autoreconf -fiv
intltoolize --force

%configure2_5x

#languages not detected
pushd po
sed -i s/"ALL_LINGUAS ="/"ALL_LINGUAS = `ls *.po | cut -d. -f1 | xargs`"/"" Makefile
popd

%make


%install
rm -rf %{buildroot}
%makeinstall


# Menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=GNOME;Graphics;GTK;Utility;
Name=Color Chooser
Name[ar]=منتقي الألوان
Name[bg]=Избор на цвят
Name[de]=Farbauswahl
Name[el]=Επιλογέας χρωμάτων
Name[en_GB]=Colour Chooser
Name[es]=Selector de colores
Name[et]=Värvivalija
Name[fi]=Värivalitsin
Name[fr]=Sélecteur de couleurs
Name[gl]=Selector de cores
Name[hu]=Színválasztó
Name[is]=Litaval
Name[it]=Selettore di colori
Name[ky]=Түс тандагыч
Name[nb]=Fargevelger
Name[nl]=Kleurenkiezer
Name[pl]=Wybór koloru
Name[pt]=Seletor de Cores
Name[pt_BR]=Seletor de cores
Name[ru]=Выбор цветов
Name[sl]=Izbirnik barv
Name[tr]=Renk Seçici
GenericName=Color Chooser
GenericName[ar]=منتقي الألوان
GenericName[bg]=Избор на цвят
GenericName[de]=Farbauswahl
GenericName[el]=Επιλογέας χρωμάτων
GenericName[en_GB]=Colour Chooser
GenericName[es]=Selector de colores
GenericName[et]=Värvivalija
GenericName[fi]=Värivalitsin
GenericName[fr]=Sélecteur de couleurs
GenericName[gl]=Selector de cores
GenericName[hu]=Színválasztó
GenericName[is]=Litaval
GenericName[it]=Selettore di colori in GTK2
GenericName[ky]=Түс тандагыч
GenericName[nb]=Fargevelger
GenericName[nl]=Kleurenkiezer
GenericName[pl]=Wybór koloru
GenericName[pt]=Seletor de Cores
GenericName[pt_BR]=Seletor de cores
GenericName[ru]=Выбор цветов
GenericName[sl]=Izbirnik barv
GenericName[tr]=Renk Seçici
Comment=GTK2 color chooser
Comment[ar]=منتقي ألوان GTK2
Comment[bg]=GTK2 Избор на цвят
Comment[de]=GTK2 Farbauswahl
Comment[el]=Επιλογέας χρωμάτων GTK2
Comment[en_GB]=GTK2 colour chooser
Comment[es]=Selector de colores en GTK2
Comment[et]=GTK2 värvivalija
Comment[fi]=Värivalitsin GTK2:lle
Comment[fr]=Sélecteur de couleurs GTK2
Comment[gl]=Selector de cores feito con GTK2
Comment[hu]=Színek kiválasztása (GTK2)
Comment[is]=GTK2 litaval
Comment[it]=Selettore di colori in GTK2
Comment[ky]=GTK2 түс тандагычы
Comment[nb]=En fargevelger for GTK2
Comment[nl]=Kleurenkiezer gebaseerd op GTK2
Comment[pl]=Wybór koloru w GTK2
Comment[pt]=Selecionador de cores GTK2
Comment[pt_BR]=Selecionador de cores GTK2
Comment[ru]=GTK2 выбор цветов
Comment[sl]=GTK+2 Izbirnik barv
Comment[tr]=GTK2 Renk Seçici
EOF

#icons
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 pixmaps/icon.png %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 pixmaps/icon.png %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 pixmaps/icon.png %{buildroot}/%_miconsdir/%name.png

%find_lang %{name}

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
