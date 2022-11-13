Name:		texlive-lkproof
Version:	20021
Release:	1
Summary:	LK Proof figure macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lkproof
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lkproof.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lkproof.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a pair of commands \infer and \deduce, that
are used in constructing LK proof diagrams.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lkproof/proof.sty
%doc %{_texmfdistdir}/doc/latex/lkproof/lkproof-doc.pdf
%doc %{_texmfdistdir}/doc/latex/lkproof/lkproof-doc.tex
%doc %{_texmfdistdir}/doc/latex/lkproof/proofeg.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
