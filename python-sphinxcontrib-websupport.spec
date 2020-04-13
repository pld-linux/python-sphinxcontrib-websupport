# NOTE: for versions >= 1.2.1 (for python 3.5+) see python3-sphinxcontrib-websupport.spec
#
# Conditional build:
%bcond_with	tests	# unit tests (require already installed package???)
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-sphinxcontrib-websupport.spec)

Summary:	Sphinx API for Web Apps
Summary(pl.UTF-8):	API Sphinksa dla aplikacji WWW
Name:		python-sphinxcontrib-websupport
# keep 1.1.x here for python2 support
Version:	1.1.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-websupport/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-websupport/sphinxcontrib-websupport-%{version}.tar.gz
# Source0-md5:	5f5be8f1fb8228fc15f01a6081e2f2e9
Patch0:		%{name}-mock.patch
URL:		https://pypi.org/project/sphinxcontrib-websupport/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.8
BuildRequires:	python-mock
BuildRequires:	python-pytest
BuildRequires:	python-six
# don't know why, test use already installed package
BuildRequires:	python-spinxcontrib-websupport = %{version}
BuildRequires:	python-sqlalchemy
BuildRequires:	python-whoosh
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.8
BuildRequires:	python3-pytest
BuildRequires:	python3-six
# don't know why, test use already installed package
BuildRequires:	python3-spinxcontrib-websupport = %{version}
BuildRequires:	python3-sqlalchemy
BuildRequires:	python3-whoosh
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
Requires:	python-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-websupport provides a Python API to easily integrate
Sphinx documentation into your Web application.

%description -l pl.UTF-8
sphinxcontrib-websupport dostarcza pythonowe API do łatwej integracji
dokumentacji tworzonej z użyciem Sphinksa w aplikacji WWW.

%package -n python3-sphinxcontrib-websupport
Summary:	Sphinx API for Web Apps
Summary(pl.UTF-8):	API Sphinksa dla aplikacji WWW
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4
Requires:	python3-sphinxcontrib

%description -n python3-sphinxcontrib-websupport
sphinxcontrib-websupport provides a Python API to easily integrate
Sphinx documentation into your Web application.

%description -n python3-sphinxcontrib-websupport -l pl.UTF-8
sphinxcontrib-websupport dostarcza pythonowe API do łatwej integracji
dokumentacji tworzonej z użyciem Sphinksa w aplikacji WWW.

%prep
%setup -q -n sphinxcontrib-websupport-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py_sitescriptdir}/sphinxcontrib/websupport
%{py_sitescriptdir}/sphinxcontrib_websupport-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_websupport-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-websupport
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/websupport
%{py3_sitescriptdir}/sphinxcontrib_websupport-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_websupport-%{version}-py*-nspkg.pth
%endif
