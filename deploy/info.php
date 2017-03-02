<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'ssh_server';
$app['version'] = '2.3.22';
$app['release'] = '1';
$app['vendor'] = 'ClearFoundation';
$app['packager'] = 'ClearFoundation';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('ssh_server_app_description');
$app['tooltip'] = lang('ssh_server_app_tooltip');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('ssh_server_app_name');
$app['category'] = lang('base_category_network');
$app['subcategory'] = lang('base_subcategory_infrastructure');

/////////////////////////////////////////////////////////////////////////////
// Controllers
/////////////////////////////////////////////////////////////////////////////

$app['controllers']['settings']['title'] = lang('base_settings');
$app['controllers']['server']['title'] = lang('base_server');
$app['controllers']['ssh_server']['title'] = lang('ssh_server_app_name');

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['requires'] = array(
    'app-network',
);

$app['core_requires'] = array(
    'app-network-core >= 1:1.4.5',
    'openssh-server >= 5.3p1',
);

$app['core_directory_manifest'] = array(
    '/var/clearos/ssh_server' => array(),
    '/var/clearos/ssh_server/backup' => array(),
);

$app['core_file_manifest'] = array(
    'sshd.php'=> array('target' => '/var/clearos/base/daemon/sshd.php'),
    'attack-detector-sshd.php' => array('target' => '/var/clearos/attack_detector/filters/sshd.php'),
    'attack-detector-sshd-ddos.php' => array('target' => '/var/clearos/attack_detector/filters/sshd-ddos.php'),
    'clearos-sshd.conf' => array(
        'target' => '/etc/fail2ban/jail.d/clearos-sshd.conf',
        'config' => TRUE,
        'config_params' => 'noreplace'
    ),
    'clearos-sshd-ddos.conf' => array(
        'target' => '/etc/fail2ban/jail.d/clearos-sshd-ddos.conf',
        'config' => TRUE,
        'config_params' => 'noreplace'
    )
);
