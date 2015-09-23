Name:           ros-jade-schunk-pg70
Version:        1.3.6
Release:        0%{?dist}
Summary:        ROS schunk_pg70 package

Group:          Development/Libraries
License:        BSD
URL:            http://www.smartroboticsys.eu/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-roscpp
Requires:       ros-jade-serial
Requires:       ros-jade-tf
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-serial
BuildRequires:  ros-jade-tf

%description
Xacro model and RS232 control node for basic communication with Schunk PG70
gripper

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Sep 23 2015 Frantisek Durovsky <frantisek.durovsky@smartroboticsys.eu> - 1.3.6-0
- Autogenerated by Bloom

