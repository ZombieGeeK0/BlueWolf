function install() {
   clear
   echo -e "\033[32m[~] Actualizando paquetes..."
   sudo apt update -y && sudo apt upgrade -y
  

   sleep 3
   which python3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] Python3 ya esta instalado."
   else
   echo -e "\033[31m\n[!] Python3 no esta instalado."
   sleep 2
   echo -e "\033[32m\n[~] Instalando python3..."
   sudo apt install python3 -y
   fi
   
   sleep 3
   which pip3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] pip3 ya esta instalado."
   else
   echo -e "\033[31m\n[!] pip3 no esta instalado."
   sleep 2
   echo -e "\033[32m\n[~] Instalando pip3..."
   sudo apt install python3-pip -y
   fi
   
   echo -e "\033[32m\n[~] Instalando requerimientos..."
   pip3 install -r requirements.txt
}

install
