%global tl_name collection-langitalian
%global tl_revision 79075

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Italian
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langitalian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langitalian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(amsldoc-it)
Requires:	texlive(amsmath-it)
Requires:	texlive(amsthdoc-it)
Requires:	texlive(antanilipsum)
Requires:	texlive(attinormativi)
Requires:	texlive(babel-italian)
Requires:	texlive(biblatex-accursius)
Requires:	texlive(codicefiscaleitaliano)
Requires:	texlive(collection-basic)
Requires:	texlive(fancyhdr-it)
Requires:	texlive(fixltxhyph)
Requires:	texlive(frontespizio)
Requires:	texlive(hyphen-italian)
Requires:	texlive(itnumpar)
Requires:	texlive(l2tabu-italian)
Requires:	texlive(latex4wp-it)
Requires:	texlive(layaureo)
Requires:	texlive(lshort-italian)
Requires:	texlive(psfrag-italian)
Requires:	texlive(texlive-it)
Requires:	texlive(verifica)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Italian.

