Name:           python-gitplier
Version:        1.0
Release:        0%{?dist}
Summary:        A Python git library

License:        LGPL-2.1-or-later
URL:            https://gitlab.com/gitplier/gitplier
Source:         %{url}/-/archive/v%{version}/gitplier-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A Python library for easy and performant querying and parsing of Git repositories.}

%description %_description

%package -n python3-gitplier
Summary:        %{summary}

%description -n python3-gitplier %_description


%prep
%autosetup -p1 -n gitplier-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l gitplier


%check
%make


%files -n python3-gitplier -f %{pyproject_files}
%doc README.md


%changelog
