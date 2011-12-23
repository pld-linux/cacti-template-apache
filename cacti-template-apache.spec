%define		template	apache
Summary:	Apache Stats
Name:		cacti-template-%{template}
Version:	0.6
Release:	3
License:	GPL v2
Group:		Applications/WWW
Source0:	http://forums.cacti.net/download/file.php?id=301#/apachestats-0.4.zip
# Source0-md5:	6d032addcc40db63c279fdcb2dbcb786
Source1:	http://forums.cacti.net/download/file.php?id=7674#/ss_apache_stats-wget.zip
# Source1-md5:	cb460f3c00707dcb960efe8c4ceff0c1
Source2:	http://forums.cacti.net/download/file.php?id=7534#/SS_Apache_Stats-curl.zip
# Source2-md5:	71112bf32403e548120b3b76eadd5a75
Patch0:		fixes.patch
URL:		http://forums.cacti.net/about17995.html
BuildRequires:	rpmbuild(macros) >= 1.554
BuildRequires:	unzip
Requires:	cacti >= 0.8.7g-6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/webapps/cacti
%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
Apache Stats for Cacti (PHP Script Server Version).

%prep
%setup -qc -a1 -a2
mv apachestats-0.4/* .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{resourcedir},%{scriptsdir}}
install -p ss_apache_stats.php $RPM_BUILD_ROOT%{scriptsdir}
cp -p SS_Apache_Stats/cacti_host_template_webserver_apache_5min.xml \
	$RPM_BUILD_ROOT%{resourcedir}

%post
%cacti_import_template %{resourcedir}/cacti_host_template_webserver_apache_5min.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt docs/*
%attr(755,root,root) %{scriptsdir}/*
%{resourcedir}/*.xml
