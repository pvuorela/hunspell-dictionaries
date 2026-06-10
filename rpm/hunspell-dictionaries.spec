Name: hunspell-dictionaries
License: BSD
Version: 20260617
Release: 1
Source0: %{name}-%{version}.tar.bz2
Source1: eki.txt
Summary: Dictionary data for Hunspell
BuildArch: noarch

%description
%{summary}.

%package all
Summary: Meta-package for all available dictionaries
License: BSD
Requires: %{name}-bg
Requires: %{name}-cs
Requires: %{name}-da
Requires: %{name}-de
Requires: %{name}-el
Requires: %{name}-en
Requires: %{name}-es
Requires: %{name}-et
Requires: %{name}-fr
Requires: %{name}-hu
Requires: %{name}-it
Requires: %{name}-lt
Requires: %{name}-lv
Requires: %{name}-nl
Requires: %{name}-no
Requires: %{name}-pl
Requires: %{name}-pt
Requires: %{name}-ro
Requires: %{name}-ru
Requires: %{name}-sk
Requires: %{name}-sl
Requires: %{name}-sv
Requires: %{name}-tr
Requires: %{name}-uk

%description all
{%summary}.

# more info about licensing also in
# https://api.libreoffice.org/share/readme/LICENSE.html#a__Dictionaries

%package bg
Summary: Bulgarian dictionary
License: GPLv2

%description bg
{%summary}.

%package cs
Summary: Czech dictionary
License: GPLv2

%description cs
{%summary}.

%package da
Summary: Danish dictionary
License: GPLv2 OR LGPLv2.1 OR MPL1.1

%description da
{%summary}.

%package de
Summary: German dictionary
License: GPLv2 OR GPLv3

%description de
{%summary}.

%package el
Summary: Greek dictionary
License: MPL1.1 OR GPLv2 OR LGPLv2.1

%description el
{%summary}.

%package en
Summary: English dictionary
License: LGPLv2.1

%description en
{%summary}.

%package es
Summary: Spanish dictionary
License: GPLv3 OR LGPLv3 OR MPLv1.1

%description es
{%summary}.

%package et
Summary: Estonian dictionary
License: EKI AND LGPLv2.1

%description et
{%summary}.

%package fr
Summary: French dictionary
License: MPLv2

%description fr
{%summary}.

%package hu
Summary: Hungarian dictionary
License: LGPLv3 OR MPLv2

%description hu
{%summary}.

%package it
Summary: Italian dictionary
License: GPLv3

%description it
{%summary}.

%package lt
Summary: Lithuanian dictionary
License: BSD

%description lt
{%summary}.

%package lv
Summary: Latvian dictionary
License: LGPLv2.1

%description lv
{%summary}.

%package nl
Summary: Dutch dictionary
License: BSD OR CC attribution 3.0 (unported)

%description nl
{%summary}.

%package no
Summary: Norwegian dictionary
License: GPLv2

%description no
{%summary}.

%package pl
Summary: Polish dictionary
License: GPLv2 or LPGLv2.1 or MPL1.1 or Apache 2.0 or CC Attribution 4.0 International

%description pl
{%summary}.

%package pt
Summary: Portuguese dictionary
License: GPLv2 OR LGPLv2.1 OR MPLv1.1

%description pt
{%summary}.

%package ro
Summary: Romanian dictionary
License: GPLv2 OR LGPLv2.1 OR MPLv1.1

%description ro
{%summary}.

%package ru
Summary: Russian dictionary
License: BSD

%description ru
{%summary}.

%package sk
Summary: Slovak dictionary
License: GPLv2 OR LGPLv2.1 OR MPLv1.1

%description sk
{%summary}.

%package sl
Summary: Slovenian dictionary
License: GPLv2 OR LGPLv2.1

%description sl
{%summary}.

%package sv
Summary: Swedish dictionary
License: GPLv3

%description sv
{%summary}.

%package tr
Summary: Turkish dictionary
License: MPLv2

%description tr
{%summary}.

%package uk
Summary: Ukrainian dictionary
License: MPLv1.1

%description uk
{%summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%install
cp %{SOURCE1} .

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp bg_BG/bg_* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp cs_CZ/cs_* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp da_DK/da_* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp de/de_DE* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp el_GR/el_GR* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp en/en_GB* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp es/es_ES* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp et_EE/et_* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp fr_FR/fr.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp hu_HU/hu_* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp it_IT/it_* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp lt_LT/lt.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp lv_LV/lv_LV.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp nl_NL/nl_NL.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp no/nb_NO.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp no/nn_NO.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp pl_PL/pl_PL.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp pt_PT/pt_PT.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp ro/ro_RO.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp ru_RU/ru_RU.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp sk_SK/sk_SK.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp sl_SI/sl_SI.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp sv_SE/dictionaries/sv_SE.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp tr_TR/tr_TR.* $RPM_BUILD_ROOT/%{_datadir}/hunspell
cp uk_UA/uk_UA.* $RPM_BUILD_ROOT/%{_datadir}/hunspell

%files all

%files bg
# GPLv2
%license bg_BG/COPYING
%{_datadir}/hunspell/bg*

%files cs
# GPLv2
%license bg_BG/COPYING
%{_datadir}/hunspell/cs*

%files da
# GPLv2
%license bg_BG/COPYING
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
%{_datadir}/hunspell/da*
# MPLv1.1
%license es/MPL-1.1.txt

%files de
# GPLv2
%license bg_BG/COPYING
# GPLv3
%license es/GPLv3.txt
%{_datadir}/hunspell/de*

%files el
# MPLv1.1
%license es/MPL-1.1.txt
# GPLv2
%license bg_BG/COPYING
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
%{_datadir}/hunspell/el*

%files en
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
%{_datadir}/hunspell/en*

%files es
# GPLv3
%license es/GPLv3.txt
# LPGLv3
%license es/LGPLv3.txt
# MPLv1.1
%license es/MPL-1.1.txt
%{_datadir}/hunspell/es*

%files et
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
# custom eki license, bsd-like
%license eki.txt
%{_datadir}/hunspell/et*

%files fr
# MPLv2
%license tr_TR/LICENSE
%{_datadir}/hunspell/fr*

%files hu
# LPGLv3
%license es/LGPLv3.txt
# MPLv2
%license tr_TR/LICENSE
%{_datadir}/hunspell/hu*

%files it
# GPLv3
%license es/GPLv3.txt
%{_datadir}/hunspell/it*

%files lt
# BSD with explicit copyrights
%license lt_LT/COPYING
%{_datadir}/hunspell/lt*

%files lv
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
%{_datadir}/hunspell/lv*

%files nl
%license nl_NL/LICENSE.txt
%{_datadir}/hunspell/nl*

%files no
# GPLv2
%license bg_BG/COPYING
%{_datadir}/hunspell/nb*
%{_datadir}/hunspell/nn*

%files pl
# GPLv2
%license bg_BG/COPYING
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
%{_datadir}/hunspell/pl*

%files pt
# GPLv2
%license bg_BG/COPYING
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
%{_datadir}/hunspell/pt*

%files ro
# GPLv2
%license bg_BG/COPYING
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
%{_datadir}/hunspell/ro*

%files ru
# BSD with copyrights
%license ru_RU/README_ru_RU.txt
%{_datadir}/hunspell/ru*

%files sk
# GPLv2
%license bg_BG/COPYING
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
%{_datadir}/hunspell/sk*

%files sl
# GPLv2
%license bg_BG/COPYING
# LGPLv2.1
%license de/COPYING_LGPL_v2.1.txt
%{_datadir}/hunspell/sl*

%files sv
# GPLv3
%license es/GPLv3.txt
%{_datadir}/hunspell/sv*

%files tr
# MPLv2
%license tr_TR/LICENSE
%{_datadir}/hunspell/tr*

%files uk
# MPLv1.1
%license es/MPL-1.1.txt
%{_datadir}/hunspell/uk*
