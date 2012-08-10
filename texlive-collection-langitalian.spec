# revision 26191
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langitalian
Epoch:		1
Version:	20120810
Release:	1
Summary:	Italian
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langitalian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-codicefiscaleitaliano
Requires:	texlive-fixltxhyph
Requires:	texlive-hyphen-italian
Requires:	texlive-frontespizio
Requires:	texlive-itnumpar
Requires:	texlive-layaureo

%description
Support for typesetting Italian.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
