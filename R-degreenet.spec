%global packname  degreenet
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2
Release:          3
Summary:          Models for Skewed Count Distributions Relevant to Networks
Group:            Sciences/Mathematics
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/degreenet_1.2.tar.gz
Requires:         R-network 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-network 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Likelihood-based inference for skewed count distributions used in network
modeling. "degreenet" is a part of the "statnet" suite of packages for
network analysis.  For a list of functions type: help(package='degreenet')

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/flo*
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
