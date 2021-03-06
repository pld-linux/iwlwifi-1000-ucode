# NOTE: currently it's included in linux-firmware.spec
Summary:	Microcode image for Intel Wireless WiFi Link 1000BGN Adapter
Summary(pl.UTF-8):	Obraz mikrokodu dla układów bezprzewodowych Intel Wireless WiFi Link 1000BGN
%define	_module	1000
Name:		iwlwifi-%{_module}-ucode
Version:	39.31.5.1
Release:	1.1
Epoch:		1
License:	distributable
Group:		Base/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
# Source0-md5:	8098503cb2abcdeffffb3ddd2d8d6f60
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The file provided in this package must be present on your system in
order for the Intel Wireless WiFi Link 1000BGN driver for Linux
(iwlwifi-%{_module}) to operate on your system.

On adapter initialization, and at varying times during the uptime of
the adapter, the microcode is loaded into the RAM on the network
adapter. The microcode provides the low level MAC features including
radio control and high precision timing events (backoff, transmit,
etc.) while also providing varying levels of packet filtering which
can be used to keep the host from having to handle packets that are
not of interest given the current operating mode of the device.

%description -l pl.UTF-8
Plik dostarczany przez ten pakiet jest wymagany w systemie do
działania linuksowego sterownika dla układów bezprzewodowych Intel
Wireless WiFi Link 1000BGN (iwlwifi-%{_module}).

Przy inicjalizacji układu i w różnych chwilach w trakcie jego
działania mikrokod jest wczytywany do pamięci RAM układu. Mikrokod
udostępnia funkcje niskopoziomowe MAC, w tym sterowanie częścią
radiową i zdarzeniami wymagającymi dużej dokładności czasowej
(oczekiwania, transmisja itp.), a także różne poziomy filtrowania
pakietów, zapobiegające docieraniu do komputera pakietów
niepotrzebnych w danym trybie pracy urządzenia.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install iwlwifi-%{_module}-5.ucode $RPM_BUILD_ROOT/lib/firmware
install LICENSE.%{name} $RPM_BUILD_ROOT/lib/firmware/%{name}-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.%{name}
/lib/firmware/%{name}-LICENSE
/lib/firmware/iwlwifi-%{_module}-5.ucode
