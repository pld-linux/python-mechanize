%define		module	mechanize
%define		extraver %{nil}
Summary:	Library for automating interaction with web pages
Summary(pl.UTF-8):	Biblioteka do automatycznej interakcji ze stronami WWW
Name:		python-%{module}
Version:	0.2.5
Release:	2
License:	BSD, ZPL 2.1
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/mechanize/src/%{module}-%{version}%{extraver}.tar.gz
# Source0-md5:	32657f139fc2fb75bcf193b63b8c60b2
URL:		http://wwwsearch.sourceforge.net/
BuildRequires:	python >= 1:2.3
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	python-ClientForm >= 0.2.6
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for automating interaction with web pages.

%description -l pl.UTF-8
Biblioteka do automatycznej interakcji ze stronami WWW.

%prep
%setup -q -n %{module}-%{version}%{extraver}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
    --root=$RPM_BUILD_ROOT \
    --optimize=2

%py_postclean %{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[oc]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/mechanize-*.egg-info
%endif
