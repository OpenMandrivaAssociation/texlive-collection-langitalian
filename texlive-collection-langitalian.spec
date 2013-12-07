# revision 30372
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langitalian
Epoch:		1
Version:	20131013
Release:	4
Summary:	Italian
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langitalian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-amsldoc-it
Requires:	texlive-amsmath-it
Requires:	texlive-amsthdoc-it
Requires:	texlive-babel-italian
Requires:	texlive-codicefiscaleitaliano
Requires:	texlive-fancyhdr-it
Requires:	texlive-fixltxhyph
Requires:	texlive-frontespizio
Requires:	texlive-hyphen-italian
Requires:	texlive-itnumpar
Requires:	texlive-l2tabu-italian
Requires:	texlive-latex4wp-it
Requires:	texlive-layaureo
Requires:	texlive-lshort-italian
Requires:	texlive-psfrag-italian
Requires:	texlive-texlive-it

%description
Support for Italian.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
