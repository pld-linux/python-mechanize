%define		module mechanize
%define		_beta b
Summary:	Library for automating interaction with web pages
Summary(pl.UTF-8):	Biblioteka do automatycznej interakcji ze stronami WWW
Name:		python-%{module}
Version:	0.1.6
Release:	0.%{_beta}.2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/mechanize/src/%{module}-%{version}%{_beta}.tar.gz
# Source0-md5:	98c27be9464f1342ede05784999d2757
URL:		http://wwwsearch.sourceforge.net/
%pyrequires_eq  python-modules
BuildRequires:  python >= 1:2.3
BuildRequires:  python-devel >= 1:2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for automating interaction with web pages.

%description -l pl.UTF-8
Biblioteka do automatycznej interakcji ze stronami WWW.

%prep
%setup -q -n %{module}-%{version}%{_beta}

%build
python setup.py build 

%install
python setup.py install \
    --root=$RPM_BUILD_ROOT \
    --optimize=2

%py_postclean %{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING.txt README.html ChangeLog.txt
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[oc]
