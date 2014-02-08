# revision 23552
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langpolish
Epoch:		1
Version:	20120224
Release:	2
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


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780452
- Update to latest release.
- Import texlive-collection-langpolish
- Import texlive-collection-langpolish

