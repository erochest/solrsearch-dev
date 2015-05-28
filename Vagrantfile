# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "chef/ubuntu-14.04"
  config.vm.network "private_network", ip: "33.33.33.8"

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.extra_vars = {
      username: 'vagrant',
      ssh_dir: './ssh',
      dotfiles: 'https://github.com/erochest/dotfiles.git',
      hostname: 'solr.dev',
      debug: true,
      ruby_ver: '2.2.1',
      solr_version: '4.10.4',
      bash_it_plugins: %w{base fasd tmux},
      bash_it_aliases: %w{bundler general vim},
      omekadir: '/var/www/omeka',
    }
  end
end
