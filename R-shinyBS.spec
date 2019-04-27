#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-shinyBS
Version  : 0.61
Release  : 11
URL      : https://cran.r-project.org/src/contrib/shinyBS_0.61.tar.gz
Source0  : https://cran.r-project.org/src/contrib/shinyBS_0.61.tar.gz
Summary  : Twitter Bootstrap Components for Shiny
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : R-htmltools
BuildRequires : R-httpuv
BuildRequires : R-mime
BuildRequires : R-shiny
BuildRequires : R-xtable
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n shinyBS

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552941798

%install
export SOURCE_DATE_EPOCH=1552941798
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinyBS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinyBS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinyBS
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  shinyBS || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/shinyBS/DESCRIPTION
/usr/lib64/R/library/shinyBS/INDEX
/usr/lib64/R/library/shinyBS/Meta/Rd.rds
/usr/lib64/R/library/shinyBS/Meta/features.rds
/usr/lib64/R/library/shinyBS/Meta/hsearch.rds
/usr/lib64/R/library/shinyBS/Meta/links.rds
/usr/lib64/R/library/shinyBS/Meta/nsInfo.rds
/usr/lib64/R/library/shinyBS/Meta/package.rds
/usr/lib64/R/library/shinyBS/NAMESPACE
/usr/lib64/R/library/shinyBS/R/shinyBS
/usr/lib64/R/library/shinyBS/R/shinyBS.rdb
/usr/lib64/R/library/shinyBS/R/shinyBS.rdx
/usr/lib64/R/library/shinyBS/examples/Alerts/server.R
/usr/lib64/R/library/shinyBS/examples/Alerts/ui.R
/usr/lib64/R/library/shinyBS/examples/Buttons/server.R
/usr/lib64/R/library/shinyBS/examples/Buttons/ui.R
/usr/lib64/R/library/shinyBS/examples/Collapses/server.R
/usr/lib64/R/library/shinyBS/examples/Collapses/ui.R
/usr/lib64/R/library/shinyBS/examples/Modals/server.R
/usr/lib64/R/library/shinyBS/examples/Modals/ui.R
/usr/lib64/R/library/shinyBS/examples/TooltipsandPopovers/server.R
/usr/lib64/R/library/shinyBS/examples/TooltipsandPopovers/ui.R
/usr/lib64/R/library/shinyBS/help/AnIndex
/usr/lib64/R/library/shinyBS/help/aliases.rds
/usr/lib64/R/library/shinyBS/help/paths.rds
/usr/lib64/R/library/shinyBS/help/shinyBS.rdb
/usr/lib64/R/library/shinyBS/help/shinyBS.rdx
/usr/lib64/R/library/shinyBS/html/00Index.html
/usr/lib64/R/library/shinyBS/html/R.css
/usr/lib64/R/library/shinyBS/tests/tipify_test.R
/usr/lib64/R/library/shinyBS/tests/tipify_test2.R
/usr/lib64/R/library/shinyBS/www/shinyBS.css
/usr/lib64/R/library/shinyBS/www/shinyBS.js
