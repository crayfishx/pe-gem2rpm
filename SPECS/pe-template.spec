# Generated from <%= format.gem_path %> by gem2rpm -*- rpm-spec -*-
%define rbname <%= spec.name %>
%define version <%= spec.version %>
%define release 1

Summary: <%= spec.summary %>
Name: pe-rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: <%= spec.homepage %>
Source: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: pe-ruby <%= spec.required_ruby_version %>
Requires: pe-rubygems >= <%= Gem::RubyGemsVersion %>
<% for d in spec.dependencies -%>
<% for req in d.requirement -%>
Requires: pe-rubygem-<%= d.name %> <%= req %>
<% end -%>
<% end -%>
BuildRequires: pe-ruby <%= spec.required_ruby_version %>
BuildRequires: pe-rubygems >= <%= Gem::RubyGemsVersion %>
BuildArch: noarch
Provides: ruby(<%= spec.name.capitalize %>) = %{version}

%define gemdir <%= Gem.dir %>
%define gembuilddir %{buildroot}%{gemdir}

%description

Packaged for Puppet Enterprise.

<%= spec.description %>

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
/opt/puppet/bin/gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
<% if ! spec.executables.empty? -%>
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin
<% end -%>

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
<% for f in spec.executables -%>
%{_bindir}/<%= f %>
<% end -%>
%{gemdir}/gems/<%= spec.name %>-<%= spec.version %>

%doc %{gemdir}/doc/<%= spec.name %>-<%= spec.version %>
%{gemdir}/cache/
%{gemdir}/specifications/

%changelog
