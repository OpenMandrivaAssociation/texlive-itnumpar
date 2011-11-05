# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/itnumpar
# catalog-date 2008-08-19 23:32:24 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-itnumpar
Version:	1.0
Release:	1
Summary:	Spell numbers in words (Italian)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/itnumpar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/itnumpar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/itnumpar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/itnumpar.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Sometimes we need to say "Capitolo primo" or "Capitolo uno"
instead of "Capitolo 1", that is, spelling the number in words
instead of the usual digit form. This package provides support
for spelling out numbers in Italian words, both in cardinal and
in ordinal form.

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
%{_texmfdistdir}/tex/latex/itnumpar/itnumpar.sty
%doc %{_texmfdistdir}/doc/latex/itnumpar/README
%doc %{_texmfdistdir}/doc/latex/itnumpar/itnumpar.pdf
#- source
%doc %{_texmfdistdir}/source/latex/itnumpar/itnumpar.dtx
%doc %{_texmfdistdir}/source/latex/itnumpar/itnumpar.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
