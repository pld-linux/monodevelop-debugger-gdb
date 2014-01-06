%include	/usr/lib/rpm/macros.mono
Summary:	GDB debugger support for MonoDevelop
Summary(pl.UTF-8):	Obsługa debuggera GDB dla programu MonoDevelop
Name:		monodevelop-debugger-gdb
%define	mainver	4.2.2
%define	subver	2
Version:	%{mainver}.%{subver}
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.mono-project.com/sources/monodevelop-debugger-gdb/%{name}-%{mainver}-%{subver}.tar.bz2
# Source0-md5:	c18d13045a9dadf3239bc00a76d5ad8c
URL:		http://monodevelop.com/
BuildRequires:	mono-csharp
BuildRequires:	monodevelop >= 4.2.2
BuildRequires:	pkgconfig
Requires:	gdb
Requires:	monodevelop >= 4.2.2
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GDB debugger support for MonoDevelop.

%description -l pl.UTF-8
Obsługa debuggera GDB dla programu MonoDevelop.

%prep
%setup -q -n %{name}-%{mainver}

%build
# not autoconf configure
./configure \
	--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Debugger/MonoDevelop.Debugger.Gdb.dll
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Debugger/MonoDevelop.Debugger.Gdb.dll.mdb
