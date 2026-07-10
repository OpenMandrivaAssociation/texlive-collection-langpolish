%global tl_name collection-langpolish
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Polish
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langpolish
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langpolish.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(babel-polish)
Requires:	texlive(bredzenie)
Requires:	texlive(cc-pl)
Requires:	texlive(collection-basic)
Requires:	texlive(collection-latex)
Requires:	texlive(gustlib)
Requires:	texlive(gustprog)
Requires:	texlive(hyphen-polish)
Requires:	texlive(lshort-polish)
Requires:	texlive(mex)
Requires:	texlive(mwcls)
Requires:	texlive(pl)
Requires:	texlive(polski)
Requires:	texlive(przechlewski-book)
Requires:	texlive(qpxqtx)
Requires:	texlive(tap)
Requires:	texlive(tex-virtual-academy-pl)
Requires:	texlive(texlive-pl)
Requires:	texlive(utf8mex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Polish.

