%define		module	mechanize
%define		extraver b
%define		rel		4
Summary:	Library for automating interaction with web pages
Summary(pl.UTF-8):	Biblioteka do automatycznej interakcji ze stronami WWW
Name:		python-%{module}
Version:	0.1.6
Release:	0.%{extraver}.%{rel}
License:	BSD
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/mechanize/src/%{module}-%{version}%{extraver}.tar.gz
# Source0-md5:	98c27be9464f1342ede05784999d2757
URL:		http://wwwsearch.sourceforge.net/
%pyrequires_eq  python-modules
BuildRequires:	python >= 1:2.3
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-setuptools
Requires:	python-ClientForm >= 0.2.6
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
%doc COPYING.txt README.html ChangeLog.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[oc]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/mechanize-*.egg-info
%endif
