Summary:	Dockapp that runs shell-scripts and displays it's output
Summary(pl.UTF-8):	Aplet uruchamiający skrypty shella i wyświetlający ich wynik
Name:		wminfo
Version:	1.51
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://kling.mine.nu/files/%{name}-%{version}.tar.gz
# Source0-md5:	dd4b168a31847694dfdb74772c57b7da
Source1:	%{name}.desktop
URL:		http://kling.mine.nu/wminfo.htm
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a dockapp that runs a (user-defined) shell-script, captures
it's output and displays it five rows at a time. You can scroll rows
up and down and scroll the rows horizontally. Useful for tailing
log-files etc.

%description -l pl.UTF-8
Aplet uruchamiający (zdefiniowany przez użytkownika) skrypt shella,
przechwytujący jego wynik i wyświetlający go jednorazowo w pięciu
rzędach. Możesz przewijać je do góry i na dół a także horyzontalnie.
Przydatny do wyświetlania logów i tym podobnych.

%prep
%setup -q -n %{name}

%build
cd wminfo
%{__make} \
	FLAGS="%{rpmcflags}" \
	LIBDIR="-L/usr/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

install wminfo/wminfo $RPM_BUILD_ROOT%{_bindir}
cp -R plugins $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/docklets/*
