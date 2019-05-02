# revision 30372
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langpolish
Epoch:		1
Version:	20190228
Release:	1
Summary:	Polish
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langpolish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-latex
Requires:	texlive-collection-basic
Requires:	texlive-babel-polish
Requires:	texlive-cc-pl
Requires:	texlive-gustlib
Requires:	texlive-gustprog
Requires:	texlive-hyphen-polish
Requires:	texlive-lshort-polish
Requires:	texlive-mex
Requires:	texlive-mwcls
Requires:	texlive-pl
Requires:	texlive-polski
Requires:	texlive-przechlewski-book
Requires:	texlive-qpxqtx
Requires:	texlive-tap
Requires:	texlive-tex-virtual-academy-pl
Requires:	texlive-texlive-pl
Requires:	texlive-utf8mex

%description
Support for Polish.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
