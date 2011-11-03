# revision 20021
# category Package
# catalog-ctan /macros/latex/contrib/lkproof
# catalog-date 2010-10-07 09:27:06 +0200
# catalog-license gpl
# catalog-version 3.1
Name:		texlive-lkproof
Version:	3.1
Release:	1
Summary:	LK Proof figure macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lkproof
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lkproof.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lkproof.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines a pair of commands \infer and \deduce, that
are used in constructing LK proof diagrams.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lkproof/proof.sty
%doc %{_texmfdistdir}/doc/latex/lkproof/lkproof-doc.pdf
%doc %{_texmfdistdir}/doc/latex/lkproof/lkproof-doc.tex
%doc %{_texmfdistdir}/doc/latex/lkproof/proofeg.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
