%define pg_lib_dir %{_prefix}/pgsql-11/lib
%define pg_keeper_commit d9a21f33fd960b28b7f0426c6f6df2b24905b3b3

Summary: Simplified clustering module for PostgreSQL
Name: pg_keeper
Version: 1.0+0.gitd9a21f
Release: 1%{?dist}.el7
URL: https://github.com/MasahikoSawada/pg_keeper

Source0: https://github.com/MasahikoSawada/pg_keeper/archive/%{pg_keeper_commit}.tar.gz#/pg_keeper.tar.gz

Patch1: Add-PQclear.patch

License: 2-clause BSD-like license

BuildRoot: %{_tmppath}/%{name}-%{pg_keeper_commit}
BuildRequires: postgresql11-devel
BuildRequires: postgresql11
BuildRequires: openssl-devel
BuildRequires: krb5-devel
BuildRequires: llvm-toolset-7
BuildRequires: llvm5.0

%description
Simplified clustering module for PostgreSQL.
pg_keeper is a simplified clustering module for PostgreSQL, to
promote a standby server to master in a 2 servers cluster.

%prep
%setup -q -n %{name}-%{pg_keeper_commit}
%patch1 -p1

%build
PATH=/usr/pgsql-11/bin:$PATH \
  %{__make} USE_PGXS=1

%install
%{__rm} -rf $RPM_BUILD_ROOT

PATH=/usr/pgsql-11/bin:$PATH \
  %{__make} DESTDIR=$RPM_BUILD_ROOT USE_PGXS=1 install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{pg_lib_dir}/pg_keeper.so
%attr(0755,root,root) %dir %{pg_lib_dir}/bitcode/pg_keeper
%{pg_lib_dir}/bitcode/*.bc
%{pg_lib_dir}/bitcode/pg_keeper/*.bc

%changelog
* Mon Sep  9 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0+0.gitd9a21f-1
- 1.0+0.gitd9a21f
