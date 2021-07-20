# Instalar un Nodo de Bitcoin Core

## Instalar una máquina virtual usando VirtualBox

https://hibbard.eu/install-ubuntu-virtual-box/

Pasos a seguir:

1. Descarga VirtualBox y una copia de Ubuntu Server.
2. Crea una nueva máquina virtual en VirtualBox (type=Linux, Version=Ubuntu (64-bit), Memory=2048 MB).
3. Selecciona como `start-up disk` el servidor de Ubuntu (eg `ubuntu-18.04.3-live-server-amd64.iso`)
4. Lleva a cabo todos los pasos de la instalación. No olvidar instalar `OpenSSH server`.
5. Correr y actualizar SSH:

```sh
sudo apt-get update
sudo apt-get upgrade

ssh # Si ssh no está instalado, usar el siguiente comando:
sudo apt-get install openssh-server
```

6. IMPORTANTE: Apaga la máquina virtual con `$ sudo poweroff` y cambia los `Settings`. En la pestaña de `Network` cambair el Adaptador 1, `Attached to: Bridged Adapter`.
7. Obtener la dirección de IP asignada con `$ ifconfig` (e.g. `192.168.0.131`).

## Corre la máquina virtual desde tu propia terminal

Para prender y apagar la máquina virtual en VirtualBox:

```sh
VBoxManage startvm "bitcoin-core-jmsx" --type headless

VBoxManage controlvm "bitcoin-core-jmsx" poweroff
```

Para tomar el control del servidor desde tu terminal:

```sh
# Mainnet
ssh jomsox@192.168.0.150

# Testnet
ssh jomsox@192.168.0.175

```

```sh
# We need to resize the logical volume to use all the existing and free space of the volume group
$ lvm
lvm> lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
lvm> exit

# And then, we need to resize the file system to use the new available space in the logical volume
$ resize2fs /dev/ubuntu-vg/ubuntu-lv
resize2fs 1.44.1 (24-Mar-2018)
Filesystem at /dev/ubuntu-vg/ubuntu-lv is mounted on /; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 58
The filesystem on /dev/ubuntu-vg/ubuntu-lv is now 120784896 (4k) blocks long.

# Finally, you can check that you now have available space:
$ df -h
Filesystem                         Size  Used Avail Use% Mounted on
udev                               3.9G     0  3.9G   0% /dev
tmpfs                              786M  1.2M  785M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv  454G  3.8G  432G   1% /

```

Usar el servidor como administrador:

```sh
sudo passwd

su - root

curl https://raw.githubusercontent.com/BlockchainCommons/Bitcoin-Standup-Scripts/master/Scripts/StandUp.sh > standup.sh

chmod +x standup.sh

# The arguments are read as per the below variables:
# ./standup.sh "PUBKEY" "BTCTYPE" "SSH_KEY" "SYS_SSH_IP" "USERPASSWORD"

# BTCTYPE Can be one of the following: "Mainnet", "Pruned Mainnet", "Testnet", "Pruned Testnet", or "Private Regtest", default is "Pruned Testnet"


./standup.sh "" "Pruned Testnet" "" "" ""

./standup.sh "" "Pruned Mainnet" "" "" ""
```

Como resultado del standup.sh, podrás consultar los logs y los errores en:

```sh
root@jomsox:/# ls -l | grep standup
# -rw-r--r--   1 root root      53151 Jul 17 18:26 standup.err
# -rw-r--r--   1 root root     101081 Jul 17 18:26 standup.log
# -rw-r--r--   1 root root        146 Jul 17 18:26 standup.uri
```

## Compilar Bitcoin desde el Código Fuente

Instala Git y demás dependencias:

```sh
sudo apt-get install git build-essential -y

sudo apt-get install libtool autotools-dev automake pkg-config bsdmainutils python3 libssl-dev libevent-dev libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-test-dev libboost-thread-dev libminiupnpc-dev libzmq3-dev libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler ccache -y

```

Para clonar la última versión del código de bitcoin core:

```sh
git clone https://github.com/bitcoin/bitcoin.git
```

Instalar Install Berkley DB v4.8

```sh
cd bitcoin/contrib/ && ./install_db4.sh `pwd`
```

Una vez terminada la istalación, debe aparecer el siguiente código en la pantalla. Guárdalo, porque después lo vamos a utilizar.

```sh
# db4 build complete.

# When compiling bitcoind, run `./configure` in the following way:

#   export BDB_PREFIX='/root/bitcoin/contrib/db4'
#   ./configure BDB_LIBS="-L${BDB_PREFIX}/lib -ldb_cxx-4.8" BDB_CFLAGS="-I${BDB_PREFIX}/include" ...
```

```sh
git tag -n | sort -V
git checkout v0.21.1
```

```sh
./autogen.sh
export BDB_PREFIX='/root/bitcoin/contrib/db4'
./configure BDB_LIBS="-L${BDB_PREFIX}/lib -ldb_cxx-4.8" BDB_CFLAGS="-I${BDB_PREFIX}/include"
make  # build bitcoin core
```
