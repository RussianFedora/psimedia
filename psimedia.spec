Name:           psimedia
Version:        1.0.3
Release:        3%{?dist}
Summary:        Audio and video RTP services for Psi-like IM clients

Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://delta.affinix.com/psimedia/
Source0:        http://delta.affinix.com/download/psimedia/%{name}-%{version}.tar.bz2
Source1:        psimedia.desktop
# Using %{_libdir}/psi/plugins directory for psimedia demo
Patch0:         psimedia-demo.patch
Requires:       psi >= 0.13

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  qt4-devel
BuildRequires:  gstreamer-plugins-base-devel >= 0.10.22
BuildRequires:  liboil-devel >= 0.3
BuildRequires:  speex-devel
BuildRequires:  desktop-file-utils

%description
PsiMedia is a thick abstraction layer for providing audio and
video RTP services to Psi-like IM clients. The implementation
is based on GStreamer.

%prep
%setup -q
%patch0 -p1

%build
# Generated by qconf 1.5 ( http://delta.affinix.com/qconf/ )
./configure --libdir=%{_libdir} --prefix=%{_prefix} --verbose

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

install -D -m 755 gstprovider/libgstprovider.so $RPM_BUILD_ROOT%{_libdir}/psi/plugins/libgstprovider.so
install -D -m 755 demo/demo $RPM_BUILD_ROOT%{_bindir}/%{name}

desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/psi/plugins/libgstprovider.so

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Alexey Kurov <nucleo@fedoraproject.org> - 1.0.3-2
- Fixed patch for using libdir in plugins path
- Group changed to Applications/Multimedia

* Mon Jul  6 2009 Alexey Kurov <nucleo@fedoraproject.org> - 1.0.3-1
- Initial RPM release
