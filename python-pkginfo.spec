Summary:	Query metadata from sdists / bdists / installed packages
Name:		python-pkginfo
Version:	1.10.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pkginfo/
Source0:	https://files.pythonhosted.org/packages/source/p/pkginfo/pkginfo-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(sphinx)
BuildArch:	noarch

%description
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distribution (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info stored
in a “development checkout” (e.g, created by running setup.py develop).

%files
%license LICENSE.txt
%doc README.txt CHANGES.txt html
%{_bindir}/pkginfo
%{py_sitedir}/pkginfo
%{py_sitedir}/pkginfo-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n pkginfo-%{version}

# remove test subpackage
sed -i "s/, 'pkginfo.tests'//g" setup.py

%build
%py_build

# docs
PYTHONPATH=${PWD} sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py_install

