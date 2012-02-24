# revision 23552
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langpolish
Version:	20120223
Release:	1
Summary:	Polish
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langpolish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-cc-pl
Requires:	texlive-gustlib
Requires:	texlive-gustprog
Requires:	texlive-mex
Requires:	texlive-mwcls
Requires:	texlive-pl
Requires:	texlive-polski
Requires:	texlive-przechlewski-book
Requires:	texlive-qpxqtx
Requires:	texlive-tap
Requires:	texlive-utf8mex
Requires:	texlive-hyphen-polish
Requires:	texlive-collection-latex
Requires:	texlive-collection-basic

%description
Support for typesetting Polish.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
