#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-velocity-tools
Version  : 2.0
Release  : 2
URL      : https://github.com/apache/velocity-tools/archive/2.0.tar.gz
Source0  : https://github.com/apache/velocity-tools/archive/2.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/velocity/velocity-tools/2.0/velocity-tools-2.0.jar
Source2  : https://repo1.maven.org/maven2/org/apache/velocity/velocity-tools/2.0/velocity-tools-2.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-velocity-tools-data = %{version}-%{release}

%description
R E A D M E
===========
Welcome to the VelocityTools projects. This is a subproject of the
Apache Velocity project hosted at http://velocity.apache.org/
The VelocityTools project contains three subprojects:

%package data
Summary: data components for the mvn-velocity-tools package.
Group: Data

%description data
data components for the mvn-velocity-tools package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/velocity/velocity-tools/2.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/velocity/velocity-tools/2.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/velocity/velocity-tools/2.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/velocity/velocity-tools/2.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/velocity/velocity-tools/2.0/velocity-tools-2.0.jar
/usr/share/java/.m2/repository/org/apache/velocity/velocity-tools/2.0/velocity-tools-2.0.pom
