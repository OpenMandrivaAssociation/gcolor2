Name:		gcolor2
Version:	0.4
Release:	%mkrel 15
Summary:	Simple color selector
Group:		Graphics
License:	GPLv2+
URL:		http://gcolor2.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/gcolor2/%{name}-%{version}.tar.bz2
Source1:	es.po
Source2:	tr.po
Source3:	it.po
Source4:	pt_BR.po  
Source5:	el.po
Source6:	sl.po
Source7:	et.po
Source8:	gl.po
Source9:	ar.po
Source10:	hu.po
Source11:	fi.po
Source12:	ky.po
Source13:	nl.po
Source14:	de.po
Source15:	nb.po
Source16:	ru.po
Patch0:		gcolor2-french.patch
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
%setup -q
%patch0 -p1
%patch1 -p1

cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	  %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} \
	  %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} po

%build
echo "gcolor2.glade" >> po/POTFILES.in

autoreconf -fiv
intltoolize --force

%configure2_5x

#languages not detected
sed -i s/"ALL_LINGUAS ="/"ALL_LINGUAS = ar de el es et fi fr gl hu it ky nb nl pt_BR ru sl tr"/"" po/Makefile

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
Name[de]=Farbauswahl
Name[el]=Επιλογέας χρωμάτων
Name[et]=Värvivalija
Name[fi]=Värivalitsin
Name[fr]=Sélecteur de couleur
Name[gl]=Selector de cores
Name[hu]=Színválasztó
Name[it]=Selettore di colori
Name[ky]=Түс тандагыч
Name[nb]=Fargevelger
Name[nl]=Kleurenkiezer
Name[pl]=Wybór koloru
Name[ru]=Выбор цветов
Name[sl]=Izbirnik barv
Name[tr]=Renk Seçici
GenericName=Color Chooser
GenericName[ar]=منتقي الألوان
GenericName[de]=Farbauswahl
GenericName[el]=Επιλογέας χρωμάτων
GenericName[et]=Värvivalija
GenericName[fi]=Värivalitsin
GenericName[fr]=Sélecteur de couleur
GenericName[gl]=Selector de cores
GenericName[hu]=Színválasztó
GenericName[it]=Selettore di colori in GTK2
GenericName[ky]=Түс тандагыч
GenericName[nb]=Fargevelger
GenericName[nl]=Kleurenkiezer
GenericName[pl]=Wybór koloru
GenericName[ru]=Выбор цветов
GenericName[sl]=Izbirnik barv
GenericName[tr]=Renk Seçici
Comment=GTK2 color chooser
Comment[ar]=منتقي ألوان GTK2
Comment[de]=GTK2 Farbauswahl
Comment[el]=Επιλογέας χρωμάτων GTK2
Comment[et]=GTK2 värvivalija
Comment[fi]=Värivalitsin GTK2:lle
Comment[fr]=Sélecteur de couleur GTK2
Comment[gl]=Selector de cores feito con GTK2
Comment[hu]=Színek kiválasztása (GTK2)
Comment[it]=Selettore di colori in GTK2
Comment[ky]=GTK2 түс тандагычы
Comment[nb]=En fargevelger for GTK2
Comment[nl]=Kleurenkiezer gebaseerd op GTK2
Comment[pl]=Wybór koloru w GTK2
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

